#!/bin/bash 
STAR --runMode genomeGenerate --genomeDir star_index --genomeFastaFiles ../data/refdata/Homo_sapiens.GRCh38.dna_rm.chromosome.21.fa --runThreadN 6
STAR --runThreadN 6 --genomeDir star_index --outSAMtype BAM SortedByCoordinate --readFilesIn ../data/reads_1.fastq ../data/reads_2.fastq --outFileNamePrefix ../data/