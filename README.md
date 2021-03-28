# Introduction

Here are materials for the Hands on workshop for RNA-Seq analysis using pyrpipe, conda and snakemake organized by [COV-IRT](https://www.cov-irt.org/), [PSC](https://www.psc.edu/), and [Wurtele lab](https://metnetweb.gdcb.iastate.edu/) at Iowa State University.
This workshop will be a hands on introduction to building RNA-Seq processing pipelines using pyrpipe, snakemake and conda. 
Slides for this workshop are available at [here](https://slides.com/urmi21/deck)


# Instructions

## clone github repo
git clone https://github.com/urmi-21/COVID_RNASeq_workshop_2021.git
## change dir
cd COVID_RNASeq_workshop_2021
## copy data files
bash prepare_data.sh

## create conda env

## install mamba for faster installation
conda install -c conda-forge mamba

## create pyrpipe environment
mamba create -n pyrpipe -c bioconda pyrpipe star=2.7.7a sra-tools=2.10.9 stringtie=2.1.4 trim-galore=0.6.6 orfipy=0.0.3 salmon=1.4.0 git snakemake

## activate the environment
conda activate pyrpipe

## test pyrpipe installation
pyrpipe -h

# Credits

### Workshop Leader 
[Urminder Singh](https://urmi-21.github.io/), Iowa State University

### Co-facilitators
Jeff Haltom
Harsha Vajjala
Sumanth Kalki 
Priyanka Bhandary


