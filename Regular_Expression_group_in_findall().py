#findall() groups
import re

phoneRegex = re.compile(r'(\+\d{2})-(\d{10})')
msg1 = 'Call me at +91-9999900000 or +91-9999911111'

print('If regex object has zero or one group, then findall() will print a list containg a string.')
print('But if regex obj has two or more group, it gives a list with each element as tuple.')

print(phoneRegex.findall(msg1))

