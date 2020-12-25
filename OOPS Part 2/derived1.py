#ensure that base class has the function that derived class needs.

from base1 import base


assert hasattr(base,'foo'),'foo not present in base class.'
#assert hasattr(base,'another'),'another function not present.'


class derived(base):
    def bar(self):
        self.foo()

d = derived()
d.bar()
