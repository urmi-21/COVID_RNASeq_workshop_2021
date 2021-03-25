from pyrpipe.runnable import *

ls=Runnable(command='ls')

ls.run('.',verbose=True)
