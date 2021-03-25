from pyrpipe.mapping import *


star=Star(genome='data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa',index='testout/testindex') # create a Star object to run STAR aligner


fq1='data/reads_1.fastq'
fq2='data/reads_2.fastq'
star.run(**{'--readFilesIn': fq1+' '+fq2})



