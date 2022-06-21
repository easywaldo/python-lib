import fnmatch
import os

for filename in os.listdir('.'):
<<<<<<< HEAD
    if fnmatch.fnmatch(filename, '[0-9].py'):
=======
    if fnmatch.fnmatch(filename, 'a???[0-9].py'):
>>>>>>> 8b3eec672ed97e4b732863df4efee59f9d446b19
        print(filename)