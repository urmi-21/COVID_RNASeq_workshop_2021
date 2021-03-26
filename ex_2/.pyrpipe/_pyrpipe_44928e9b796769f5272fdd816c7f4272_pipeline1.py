"""
A simple first RNA-Seq processing pipeline

This pipeline will take raw reads and align them to genome
"""
from pyrpipe.sra import *
from pyrpipe.mapping import *


# some vaiable
fq1='../data/reads_1.fastq'
fq2='../data/reads_2.fastq'
gen='../data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa'
starindex='star_index'
hisat2index='hisat2_index'

srr_object=SRA(fastq=fq1,fastq2=fq2) # create sra object to store fastq data

#star=Star(genome=gen,index=starindex) # create a star object
#star.perform_alignment(srr_object) # perform alignment of reads using the star index

# use hisat
hisat2=Hisat2(genome=gen,index=hisat2index) # create a hisat2 object
hisat2.perform_alignment(srr_object) # perform alignment of reads using the hisat2 index




