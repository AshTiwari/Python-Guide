#public and private attribute and method.

class hello:
    def __init__(self,name,roll):
        self.__name  = name
        self.roll = roll

    def public(self):
        print('-Can be called from outside the class.')
        self.__private()

    def __private(self):
        print('-Cannot be called from outside the function.')

Hello = hello('ashu',1)


print('Access public arg: roll no.')
print('-'+ str(Hello.roll))

#print('\n')

print('Access public functions.')
Hello.public()

print('\n\n')


print('Access private arg: name.')
try:
    print(Hello.__name)
except AttributeError:
    print('-Failed')

#print('\n')

print('Access private function.')
try:
    Hello.private()
except AttributeError:
    print('-Failed')
