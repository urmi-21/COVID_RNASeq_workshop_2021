"""
A simple first RNA-Seq processing pipeline

This pipeline will take raw reads and align them to genome
"""

from pyrpipe.sra import *
from pyrpipe.mapping import *
from pyrpipe.qc import *


# some vaiable
fq1='../data/reads_1.fastq'
fq2='../data/reads_2.fastq'
gen='../data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa'
starindex='star_index'

srr_object=SRA(fastq=fq1,fastq2=fq2) # create sra object to store fastq data

# first trim the reads using trimgalore

trimgalore=Trimgalore()

trimmed_fq=trimgalore.perform_qc(srr_object)

# create new SRA object with trimmed fq
trimmed_srr_object=SRA(fastq=trimmed_fq[0], fastq2=trimmed_fq[1])

star=Star(genome=gen,index=starindex) # create a star object
star.perform_alignment(trimmed_srr_object) # perform alignment of reads using the star index





