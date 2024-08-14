# copy file() = copies contents of a file
# copy() =      copyfile() + permissiion mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)


import shutil

shutil.copyfile('test.txt.txt','copy.txt.txt')   #src,dst