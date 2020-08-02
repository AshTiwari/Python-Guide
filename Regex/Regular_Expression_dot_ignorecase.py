#ignore caps in dot cahracter

import re

msg = 'Message: Printing all vowels ignoring Case using re.I or re.IGNORECASE.'
print(msg)

print('Printing all vowels ignoring Case using re.IGNORECASE.')
vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE)       #only lower case vowels are searched
                                                        #but re.IGNORECASE ignores Case.
print(vowelRegex.findall(msg))

print('\nPrinting all vowels ignoring Case using re.I.')
vowelRegex = re.compile(r'[aeiou]',re.I)       #only lower case vowels are searched
                                                        #but re.I ignores Case.
print(vowelRegex.findall(msg))





