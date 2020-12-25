#named tuple functions.

from collections import namedtuple

student = namedtuple('student','name age')

print('Functions in namedtuple.')


print('\nPrint field of tuple.')

print(student._fields)



s1 = ('Ash',21)
s2 = ('Ashu',22)

print('\nPrinting tuple of namedtuple.')
t = (s1, s2)
print(t)

print(type(t[1]))

