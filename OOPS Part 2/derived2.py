#ensure that derived class has the function that base class needs.
#base class forcing constraints on derived class.

# constraint => derived class should have bar method.


# Method 1: Metaclass.

from base2 import base

class derived(base):
    def bar(self):
        self.foo()

d = derived()
d.bar()
