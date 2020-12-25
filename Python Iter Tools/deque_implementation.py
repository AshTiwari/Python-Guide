#implement double ended queue.

from collections import deque

deque = deque()

print(deque)
print('Type of deque: '+ str(type(deque)))

print('Append.')
deque.append(1)
deque.appendleft(0)
deque.append(3)
print(deque)


#updating deque
print('Update.')
deque[2]=2
#same as insert(i,a)
deque.insert(2,2)
print(deque)


print('Pop left')
deque.popleft()
print(deque)

print('Pop')
deque.pop()
print(deque)


