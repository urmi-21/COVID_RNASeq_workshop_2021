from pyrpipe.sra import *

#Download fastq from NCBI-SRA 
sra_object=sra.SRA('SRR1583780',directory='sra_test')

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

#initialize using existing fastq
sra_object2=sra.SRA(fastq='sra_test/SRR1583780/SRR1583780_1.fastq',fastq2='sra_test/SRR1583780/SRR1583780_2.fastq')
sra_object2.fastq_exists()

#using single-end
sra_object_single=sra.SRA(fastq='sra_test/SRR1583780/SRR1583780_1.fastq')
sra_object_single.layout

#delete files
sra_object_single.delete_fastq()





