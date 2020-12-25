#counter initialization.

from collections import Counter

print('Initalize.')
print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(Counter({'a':2, 'b':3, 'c':1}))
print(Counter(a=2, b=3, c=1))

print('\n')
print('Updating')
c = Counter(a=2, b=3, c=1)
c['a'] = 4
print(c)

print('\n')
print('update() function adds and not change.')
c.update({'c':1})
print(c)

print('\n')
print('Type of c: '+ str(type(c)))

print('\n')
print('Acces count of an element.')
print(c['a'])
print(c.get('a'))
