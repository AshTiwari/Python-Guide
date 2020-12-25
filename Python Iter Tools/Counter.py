# counter

from collections import Counter

c = Counter('Ashutosh')
print(c)


print('\n')
print('c.copy() fucntion creates a different and unrelated copy.')
c1 = c.copy()
print(c1)

print('\n')
print('c.elements')
print('elements()')
print(list(c.elements()))


'''
print('\n')
print('')
c.fromkeys

'''
print('\n')
print('c.item() function convert to a dict_item of (elem, cnt) pairs where elements are in original order.')
print(c.items())


'''
print('\n')
print('')
c.keys

'''
print('\n')
print('k most common occurence.')
print(c.most_common(2))
print('k least common occurence. c.most_common()[:-n-1:-1]')
print(c.most_common()[:-2-1:-1])


'''
print('\n')
print('c.pop()')
c.pop()
print(c)


print('\n')
print('c.popitem()')
c.popitem(u)
print(c)

print('\n')
print('')
c.setdefault
'''

print('\n')
print('Upadte fills any empty counter or adds value in existing counter.')
c.update({'z':1})
print(c)

print('\n')
print('c.subtract(d) is same as c-d')
c.subtract(Counter({'z':1}))
print(c)



print('\n')
print('c.values() gives total count.')
c.values
print(c)

print('\n')
print('c.clear() clears all counts')
c.clear()
print(c)

print('\n\n')
print('Negative and combination counnter.')
c1 = Counter(a = 2,b = 3,c = 0, d = -3)
c2 = Counter(a = 2,b = 1,c = 1, d = 4)

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print( '\nSubtraction:')
print(c2 - c1)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)

