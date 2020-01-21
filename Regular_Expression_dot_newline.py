#newline in dot.

import re

msg = 'Dear sir/madam,\nThank you for your help.\n'
print(msg)

print('\nPrinting the default dot without newline.')
noNewlineRegex = re.compile(r'.*')
print(noNewlineRegex.findall(msg))


print('\nIncluding newline in dot character using re.DOTALL')
newLineRegex = re.compile(r'.*',re.DOTALL)
print(newLineRegex.findall(msg))
