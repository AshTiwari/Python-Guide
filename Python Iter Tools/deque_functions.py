#functions of deque.

from collections import deque

deque = deque([1,2,3])


#extend vs aappend

print('Extend function.')
deque.extend('456')
deque.extend([7,8,9])
print(deque)

print('Append function.')
deque.append('abc')
deque.append(['d','e','f'])
print(deque)


#other functions.

print('Search index.')
# index(ele, beg, end)
print(deque.index(7,5,9))

print('Count')
print(deque.count(0))

print('Extend Left')
deque.extendleft([0])
print(deque)

print('Remove first occurence.')
deque.remove('abc')
print(deque)

print('Rotate by 2.')
deque.rotate(2)
print(deque)

print('Rotate left by 2.')
deque.rotate(-2)
print(deque)

print('Reverse.')
deque.reverse()
print(deque)








