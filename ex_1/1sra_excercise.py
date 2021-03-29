"""
Simple example to understand the SRA class

Run the following commands in python CLI
Example:
>>> from pyrpipe.sra import *
>>> sra_object=SRA('SRR1583780',directory='sra_test')

"""

from pyrpipe.sra import *

# Download fastq from NCBI-SRA 
sra_object=SRA('SRR1583780',directory='sra_test')

#check some attributes
sra_object.fastq_path
#'sra_test/SRR1583780/SRR1583780_1.fastq'
sra_object.fastq2_path
#'sra_test/SRR1583780/SRR1583780_2.fastq'
sra_object.directory
#'sra_test/SRR1583780'
sra_object.srr_accession
#'SRR1583780'
sra_object.layout

# initialize using existing fastq files
sra_object2=SRA(fastq='sra_test/SRR1583780/SRR1583780_1.fastq',fastq2='sra_test/SRR1583780/SRR1583780_2.fastq')
sra_object2.fastq_exists()

#using single-end
sra_object_single=SRA(fastq='sra_test/SRR1583780/SRR1583780_1.fastq')
sra_object_single.layout

#delete files
sra_object_single.delete_fastq()
sra_object_single.fastq_exists()

# download again
sra_object.delete_fastq()
sra_object=SRA('SRR1583780',directory='sra_test')


# using accession and directory
myrun=SRA('SRR1',directory='../data/fastq_data/')



