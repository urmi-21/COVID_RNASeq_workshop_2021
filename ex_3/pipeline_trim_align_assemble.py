"""
This example shows flexible parameter management using pyrpipe 
This pipeline will take raw reads and align them to genome
"""

from pyrpipe.sra import *
from pyrpipe.mapping import *
from pyrpipe.qc import *
from pyrpipe.assembly import *
from pyrpipe import _dryrun


# some vaiable
fq1='../data/reads_1.fastq'
fq2='../data/reads_2.fastq'
gen='../data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa'
starindex='star_index'

srr_object=SRA(fastq=fq1,fastq2=fq2) # create sra object to store fastq data

# first trim the reads using trimgalore

trimgalore=Trimgalore() #can override threads here

trimmed_fq=trimgalore.perform_qc(srr_object)

# create new SRA object with trimmed fq
trimmed_srr_object=SRA(fastq=trimmed_fq[0], fastq2=trimmed_fq[1])

star=Star(genome=gen,index=starindex) # create a star object
bam=star.perform_alignment(trimmed_srr_object) # perform alignment of reads using the star index; returns bam file

# create a stringtie object to perform transcript assembly
stringtie=Stringtie(threads=5)

gtf=stringtie.perform_assembly(bam)

# print gtf file
N=5
with open(gtf) as fi:
    head = [next(fi) for x in range(N)]
print(''.join(head))

if not _dryrun:
    # open the gtf
    with open(gtf) as f:
        i=0
        for l in f:
            i+=1
            print(l)
            if i >5:
                break
else:
    print('This was a dry run. GTF file will be saved to {}'.format(gtf))




