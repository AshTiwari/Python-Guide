# dot and star character.

import re

msg = 'Pick out word ending with mat:(cat hat cap ball diplomat.)'
print(msg)

dotRegex = re.compile(r'.at')            #dot means any character
print('3 letter Word ending with at using dot character.')
print(dotRegex.findall(msg))

msg  = 'Hello I am Robocop.'
print(msg)

dotAndStarRegex = re.compile(r'Hello (.*) Robocop')
print('All Word between Hello and Robocop.')
print(dotAndStarRegex.findall(msg))


