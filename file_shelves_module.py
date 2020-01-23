#shelve file module.

import shelve

#shelves are binary files.
#shelve.open() returns a dictionary-like shelf value.



#returns a shelf file object.
shelfFile = shelve.open('C://GitHub Projects//Python-Guide//Shelve_Folder//shelve_data')

shelfFile['tech'] = ['AI','ML','DL']
tech = shelfFile['tech']
print(tech)

shelfFile['lang'] = ['Python','C','C++']
lang = shelfFile['lang']
print(lang)

shelfFile['comp'] = ['Google','IBM','AMAZON']
comp = shelfFile['comp']
print(comp)


print('\nPrinting all keys.')
keys = shelfFile.keys()
print(keys)
print(list(keys))

print('\nPrinting all values.')
values = shelfFile.values()
print(values)
print(list(values))




