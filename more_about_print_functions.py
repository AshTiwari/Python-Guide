# more about functions.

#print function
print('#print() function returns \'None\'')
print('Printing a string variable.')
x= 'Hello'
print(x)

print('Printing a message.')
print('Hello')

'''
When we type a string in interactive shell,
it prints with a quote because it returns a string.

print() function displays the message and not returns a string.
Hence no quotes are attached with it.
print() function on there other hand returns 'None'.
That 'None' is not dispalyed.

If a function dosen't have a return value, it returns 'None'.
'''

print('Checking with if condition if print() return None.')
spam = print()
if spam == None:
    print('Print returned None.')




print(' \n \n')

      


#Keyword Argument
'''
Some functions have keyword argument.
These are optional arguments passed to function.They are rarely and ocasionally used.

eg. print() function have 'end' and 'sep' argumenets.
'''
print('#Keyword Argument sep and end')
print('Output when we dont pass an end argument.')
print('Hello')
print('World')
print('Output when we pass an end argument.')
print('Hello',end='*')
print('World')

#end:
'''
print function automatically add a new line when it ends.
print('Hello')
print('World')
O/P
=>
Hello
World

If we don't want a new line between two different print()statement,
but we want some other character, we can pass an end statement.
'''

print('Output when we dont pass a sep argument.')
print('cat','dog','rabbit')
print('Output when we pass a sep argument.')
print('cat','dog','rabbit',sep='*')

#sep:
'''
print() function by default seprates its different argument with a space.
But we can change that to anything we want with sep argument.
'''


