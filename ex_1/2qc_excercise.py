"""
Simple example to understand the qc module and its classes

Run the following commands in python CLI
Example:
>>> from pyrpipe.qc import *
"""

#Run these commands in python CLI

from pyrpipe.qc import *

trimgalore=Trimgalore(threads=6)

#some atributes
trimgalore._category
#'RNASeqQC'
trimgalore._command
#'trim_galore'


trimmed_fastq=trimgalore.perform_qc(sra_object) # run trimgalore and return trimmed

# Run trimgalore passing all the parameters
trimgalore.run('--paired','sra_test/SRR1583780/SRR1583780_1.fastq','sra_test/SRR1583780/SRR1583780_2.fastq')

