from pyrpipe.sra import *
from pyrpipe.quant import *
from pyrpipe.qc import *

# create objects
trimgalore=Trimgalore()
salmon=Salmon(index='../data/fastq_data/salmon_index',transcriptome='../data/fastq_data/tr.fa')

# create srr object
srr_object=SRA(srr_accession='SRR1',directory='../data/fastq_data')

# processing pipeline
srr_object.trim(trimgalore).quant(salmon)

