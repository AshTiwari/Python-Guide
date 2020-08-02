# Built in Function


#1. there are many biult in functions in python like:
print('Output of inbuilt print function')
print(5)
list1=[1,2]
sum(list1)
int()
print('\n')


#2.Standard library

'''
-Standard libraries are set of modules.
-Each module is a python program containing related functions.
-functions ofa module can be used only after we import it.

- Two style of import.

1. direct import
To call a function inside a module, we will have to write module.function().

2. from import
Here, thw whole module is imported so we don't have to write modules name.
Instead, we only call function.
'''

import random
x=random.randint(1,10)
print('O/P of standard module function randint.')
print(x)

from random import *        # '*' means 'all'
x=randint(1,10)
print(x)
print('\n')

#examples of inbuilt standard modules.

print('To exit a program prematurely use sys.exit() ')
print('\n')
import sys
#sys.exit()      



#Third party module.
'''
-installed using third party module.
-eg. pip intsall pyperclip.
-if using the function of third party modules like
    import error: No module named 'xxx'
then the third party module is not properly installed.

-pyperclip is used to copy and past from clipboard.
'''
print('Run the following snippet on interactive shell.')
print('import pyperclip \npyperclip.copy(\'Hello World\') \npyperclip.paste() ')
print('\n')

import pyperclip
pyperclip.copy('Hello World')
pyperclip.paste()




