#find and substitue using sub()

import re

msg1 = 'Agent Smith gave the document to Agent Tiger.'
print('Message: '+msg1+'\n')
nameRegex = re.compile(r'Agent \w+')
new_msg1 = nameRegex.sub('REDACTED', msg1)

print('Printing substituted value.')
print(new_msg1)

#group() in sub()

print('\nGroup in sub()\n')

nameRegex = re.compile(r'(Agent) (\w+)')
new_msg1 = nameRegex.sub(r'RAW \1 \2', msg1)    #\n means nth group.

print('Printing substituted groups.')
print(new_msg1)
