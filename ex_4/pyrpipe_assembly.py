"""
This example demonstrats pyrpipe SRA class' chaining methods for easy rna-seq pipelines

"""

from pyrpipe.sra import *
from pyrpipe.mapping import *
from pyrpipe.qc import *
from pyrpipe.assembly import *

# create objects
trimgalore=Trimgalore()
star=Star(index='../data/fastq_data/star_index')
stringtie=Stringtie(threads=5)

# create srr object
srr_object=SRA(srr_accession='SRR1',directory='../data/fastq_data')

# processing pipeline
srr_object.trim(trimgalore).align(star).assemble(stringtie)


