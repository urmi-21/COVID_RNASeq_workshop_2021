"""
A simple first RNA-Seq processing pipeline

This pipeline will take raw reads and align them to genome

Execute this pipeline as:

python pipeline_align.py --threads 10 --dry-run #execute in dry run mode

python pipeline_align.py --threads 10
or
pyrpipe --in pipeline_align.py --threads 10 
"""

from pyrpipe.sra import *
from pyrpipe.mapping import *


# some vaiable
fq1='../data/reads_1.fastq'
fq2='../data/reads_2.fastq'
gen='../data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa'
starindex='star_index'

srr_object=SRA(fastq=fq1,fastq2=fq2) # create sra object to store fastq data

star=Star(genome=gen,index=starindex,threads=10) # create a star object
star.perform_alignment(srr_object) # perform alignment of reads using the star index





