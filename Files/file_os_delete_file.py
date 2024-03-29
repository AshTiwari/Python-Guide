#deleting files.

import os

os.path.isfile('D://f1.txt')
os.path.isdir('D://f1')

#for deleting files, access is denied.
#PermissionError: [WinError 5] Access is denied: 'C://Users//MSI//Desktop//folder'
#We can try to delete folder by changing user account control.

#Alternatively, we can check that the programming is running by typing command
#on python website.


#unlink() for txt files
open('D://text.txt','w')
print('File created.')
os.unlink('D://text.txt')      #delete file
print('File deleted.')

try:
    os.mkdir('D://folder')
except FileExistsError:
    pass
try:
    os.unlink('D://folder')        #delete folder
except PermissionError:
    print("Python dosen't have permission to delete the folderon this OS.")


#rmdir for directories.
#NOTE:  Only deltes empty folder.
try:
    os.mkdir('D://fold:er2')
except FileExistsError:
    pass
try:
    os.rmdir('D://folder2')        #only deletes empty folder.
except PermissionError:
    print("Python dosen't have permission to delete the folder on this OS.")



