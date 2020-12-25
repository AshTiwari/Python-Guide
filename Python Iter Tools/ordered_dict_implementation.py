#ordered Dictionary

from collections import OrderedDict

print('Dictionary are ordered since python 3.6')

default_dict = {}

default_dict['a']=1
default_dict['b']=2
default_dict['c']=3

print('Display default Dictionary.')
print(default_dict)


ordered_dict = OrderedDict(default_dict)

print('\n')
print('Ordered Dictionary.')
print(ordered_dict)




