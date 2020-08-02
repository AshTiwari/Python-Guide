#abstract classes
# ABC- Abstract Base Class and abstractmethod

from abc import ABC, abstractmethod

print('abstract method is the method user must implement in the child class.')
print('abstract method cannot be instantiated outside child class.')
print('\n\n')

class parent(ABC):
    def __init__(self):
        pass

    @abstractmethod         #it is a decorator.
    def square():
        pass

class child(parent):
    def __init__(self,num):
        self.num = num

    def square(self):           # if not implemented here, it will give TypeError:
        return self.num**2


Child =child(5)
print(Child.square())


try:
    Parent =parent()
except TypeError:
    print('Cant instantiate abstract class.')



