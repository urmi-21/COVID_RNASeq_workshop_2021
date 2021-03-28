"""
Simple example to understand the Runnable class.
Runnable class is responsible for executing all the linux commands via the run function
All classes extenting Runnable will have a run method

Run the following commands in python CLI
Example:
>>> from pyrpipe.runnable import *
"""

from pyrpipe.runnable import *

ls=Runnable(command='ls')

ls.run('.',verbose=True)

# All classes extending Runnable have run method example
# trimgalore.run('--paired','sra_test/SRR1583780/SRR1583780_1.fastq','sra_test/SRR1583780/SRR1583780_2.fastq')

