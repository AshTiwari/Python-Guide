#deleting files.

import os


#for deleting files, access is denied.
#PermissionError: [WinError 5] Access is denied: 'C://Users//MSI//Desktop//folder'
#We can try to delete folder by changing user account control.


#unlink()
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
    print("Python dosen't have permission to delete the folder.")


#rmdir
try:
    os.mkdir('D://fold:er2')
except FileExistsError:
    pass
try:
    os.rmdir('D://folder2')        #only deletes empty folder.
except PermissionError:
    print("Python dosen't have permission to delete the folder.")



