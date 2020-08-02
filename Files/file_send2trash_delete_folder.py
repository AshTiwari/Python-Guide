#delete to bin using send2trash

from send2trash import send2trash
import os

try:
    os.mkdir('D://folder1')
    os.mkdir('D://folder1//folder2')
except FileExistsError:
    pass
print('Nested folder created.')

open('D://folder1//folder2//text.txt','w')

send2trash('D://folder1')
print('Root folder send to trash.')


################
# error: not deleting files.
################
