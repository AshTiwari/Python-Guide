# shell utilities module
# used for copying, pasting, renaming files.. for large files.

import shutil

#copy and rename.
try:
    shutil.copy('C://Users//MSI//Desktop//text.txt','D://copied_frm_dxtp.txt') #returns destination address.
except FileExistsError:
    print('File already exists.')
    
#Copy entire folder/tree and rename.
try:
    shutil.copytree('D://folder1','E://folder2//folder3')
except FileExistsError:
    print('Folder already exist.')

#move and rename a file.
shutil.move('D://copied_frm_dxtp.txt','D://folder1//file.txt')

#cannot rename directly. use move to rename.
