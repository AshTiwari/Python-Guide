#caret and dollar character

import re

print('^ means start with. $ means end with.')
msg1 = 'Hello, I am an Robocop'
msg2 = 'Hii, Hello, I am Robocop .'

beginswithRegex = re.compile(r'^Hello')     #string start with Hello.
endswithRegex = re.compile(r'Robocop$')     #string end with Robocop.

                             
print('Message:"Hello, I am an Robocop"')
print(beginswithRegex.findall(msg1))
print(endswithRegex.findall(msg1))

print('Message:"Hii, Hello, I am Robocop ."')
print(beginswithRegex.findall(msg2))
print(endswithRegex.findall(msg2))

#################
''' Try to create a regex object which check start_with and end_with in same statement.'''
#################

###########  yet to complete.
