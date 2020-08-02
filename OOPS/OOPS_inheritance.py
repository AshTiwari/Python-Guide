#inheritance
  
class parent:
    land = 2000
    shares = 3000
    __worth = 4000
    def __init__(self):
        self.money = 1000

    def party(self):
        print('-Child class/ child class can inherit public functions or arguments.')

    def __respect(self):
        print('-Child class/child class cannot inherit private function or argument.')

class child(parent):
    land = 200
    def __init__(self):
        self.money = 100
    def selffunct(self):
        print('-Child can access its own function and args.')

Child = child()

print('Accessing childs functions and arguments.')
Child.selffunct()
print('-' + str(Child.money))           #childs __init__ overrides parents.
print('-' + str(Child.land))            #childs arg overrides parents.
print('\n')

print('Accessing parents functions and arguments.')
Child.party()

try:
    Child.respect()
except AttributeError:
    print('Child cannot access parents private function.')

    
print('-' + str(Child.shares))
try:
    print('-' + str(Child.__worth))
except AttributeError:
    print('Cannot access parents private argument.')

    
