# important modules

#1
import sys
#sys.exit()     #Used to end program prematurely.


#2
import pyperclip                #used to copy and paste stuff at clipboard
pyperclip.copy('HELLO')

#if we copy something outside the python program and pyper paste it on a variable,
#the variable will store the data.
vaariable = pyperclip.paste()               

#3
import re

regex = re.compile(r'.')
mo = regex.search('message')
mo.group()
regex.findall('message')

#4
