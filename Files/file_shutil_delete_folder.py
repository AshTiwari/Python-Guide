#delete folder using shutil

import shutil
import os

try:
    os.mkdir('D://folder1')         #create folder
except FileExistsError:
    pass
print('Folder created.')

open('D://folder1//text.txt','w')   #create a file in the folder.

shutil.rmtree('D://folder1')
print('folder deleted.')

shutil.remove('D://file1.txt')
print('File Deleted')

#CAUTION: This method will permanently delete the foleders and files.
#for sending files to bin, use send2trash module.
