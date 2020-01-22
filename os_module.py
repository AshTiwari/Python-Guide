#os module

import os

#join the parameters to make a path suitable for the os it is working on
print('\nos.path.join() prints os suitable path.')
print(os.path.join('root folder','folder','file.txt'))   

print('\nos.getcwd() prints current working directory.')
print(os.getcwd())

print('\nos.chdir() changes current working directory.')
os.chdir('C://')
print(os.getcwd())

print('\nIf file is present in current directory absolute path is not required')
print('Relative path i.e file name is sufficient.')
print('But, for files not present in current directory we need absolute file.')


print('\nNotation \t Meaning')
print('. \t\t current directory')
print('.. \t\t parent directory')

print('os.path.abspath() gives the absolute path of a file.')
print(os.path.abspath('users'))

print('\nos.path.isabspath() tells if a path is absolute path or not.')
path = os.path.isabs('C://users')
print(path)


print('\nos.path.relpath() gives relative path between first and second argument.')
path = os.path.relpath('C://users//folder1//folder2','C://users')
print(path)
path = os.path.relpath('C://users','C://users//folder1//folder2')
print(path)


print('\nSeprating directory name and base name.')
dirname = os.path.dirname('C://users//folder1//folder2//spam.png')
print(dirname)
basename = os.path.basename('C://users//folder1//folder2//spam.png')
print(basename)


print('\nCheck if a path exists.')
print(os.path.exists('C://users//folder1//folder2//spam.png'))
print(os.path.exists('C://users'))
print(os.path.exists('C:\Windows\System32//calc.exe'))


print('\nCheck is path belong to file or folder and actually exist.')
print(os.path.isfile('C:\Windows\System32//calc.exe'))
print(os.path.isdir('C:\Windows\System32'))


print('\nGet size of file and list of files in a folder.')
print(os.path.getsize('C:\Windows\System32//calc.exe'))
print(os.listdir('C://'))







