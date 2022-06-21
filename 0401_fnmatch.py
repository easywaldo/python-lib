import fnmatch
import os

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '[0-9]*[a-z]*.py'):
        print(filename)