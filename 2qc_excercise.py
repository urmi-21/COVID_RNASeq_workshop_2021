#Run these commands in python CLI

from pyrpipe.qc import *

trimgalore=Trimgalore()

#some atributes
trimgalore._category
#'RNASeqQC'
trimgalore._command
#'trim_galore'

trimgalore.run('--paired','sra_test/SRR1583780/SRR1583780_1.fastq','sra_test/SRR1583780/SRR1583780_2.fastq')

