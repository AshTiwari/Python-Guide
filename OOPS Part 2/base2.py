#ensure that derived class has the function that base class needs.
#base class forcing constraints on derived class.

# constraint => derived class should have bar method.


# Method 1: Metaclass.

class BaseMeta(type):
    def __new__(cls, name,bases, body):
        print('BaseMeta.__new__',cls,name,bases,body)

        if not 'bar' in body:
            raise TypeError('derived dosent have bar method.')
        return super().__new__(cls,name,bases,body)


class base(metaclass=BaseMeta):
    def foo(self):
        print('Printing from base class.')



print('Fix the code.')
