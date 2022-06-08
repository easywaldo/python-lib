import glob
import os
import shutil

for file_path in glob.glob('%s/*.txt' % os.getcwd()):
    parent = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    new_path = os.path.join(parent, 'archive', file_name)
    shutil.move(file_path, new_path)
    
import pathlib

for p in pathlib.Path.cwd().glob('%.txt'):
    new_p = p.parent.joinpath('archive', p.name)
    p.replace(new_p)
