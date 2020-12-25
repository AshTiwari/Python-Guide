#named tuple.

from collections import namedtuple


print('Named tuple gives names  to index of a tuple.\n')

#namedtuple is a factory that returns a subclass. student is a subclass.
#Student is the name of the class that nametuple returns. It has no other use than just implentation rule.
#It is convention to have same variable name(here 'student') and class name('Student').
#name and age are field names.


student = namedtuple('Student',['name','age'])
student = namedtuple('Student','name,age')
student = namedtuple('Student','name age')

student1 = student('Ash',21)

print(student1)

print('Printing value of each index.')
print(student1.name)
print(student1.age)







