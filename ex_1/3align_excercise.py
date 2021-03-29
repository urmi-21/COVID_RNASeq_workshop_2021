"""
Simple example to understand the mapping module and its classes

Run the following commands in python CLI
Example:
>>> from pyrpipe.mapping import *
"""

from pyrpipe.mapping import *


star=Star(genome='../data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa',index='testindex', threads=10) # create a Star object to run STAR aligner

star.perform_alignment(sra_object)

fq1='../data/reads_1.fastq'
fq2='../data/reads_2.fastq'
star.run(**{'--readFilesIn': fq1+' '+fq2})



