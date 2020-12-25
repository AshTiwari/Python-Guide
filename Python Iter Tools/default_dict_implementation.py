#default dict

from collections import defaultdict

print('Note: default_dict is faster than setdefault() function of dict.')



d = defaultdict(lambda: -1)

d['a']=1
d['b']=2

print(list(d))

print(type(d))

print('\n')
print('Accesing value.')
print(d['a'])
print(d['b'])
print(d['c'])


print('\n')
print('Changing default value to empty list.')
d = defaultdict(list)

d['a']=1
d['b']=2

print('Accesing value.')
print(d['a'])
print(d['b'])
print(d['c'])
print(list(d))

