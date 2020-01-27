#walking a directory tree.

import os

#create  a directory tree.

def createDir(absname):
    try:
        os.mkdir(absname)
    except FileExistsError:
        pass

def createFile(absname):
    try:
        open(absname,'w')
    except:
        pass

createDir('D://folder1')
createDir('D://folder1//folder11')
createDir('D://folder1//folder12')
createFile('D://folder1//text11.txt')
createFile('D://folder1//text12.txt')
createDir('D://folder1//folder11//folder111')
createDir('D://folder1//folder11//folder112')
createFile('D://folder1//folder11/text111.txt')
createFile('D://folder1//folder11/text112.txt')
createDir('D://folder1//folder12//folder121')
createDir('D://folder1//folder12//folder112')
createFile('D://folder1//folder12/text121.txt')
createFile('D://folder1//folder12/text122.txt')


#walk the directory tree and print it.

for folder, subfolder, file in os.walk('D://folder1'):
    print('The folder name is: '+str(folder))
    print('The subfolders present in '+folder+' are: ')
    for subfolders in subfolder:
        print('\t'+subfolders)
    print('The files present in ' +folder+ ' are: ')
    for files in file:
        print('\t'+files)
    print()
    
    
