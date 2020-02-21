#multiple  inheritance

class parent1:
    def __init__(self):
        print('__init__ of parent1 called.')

class parent2:
    def __init__(self):
        print('__init__ of parent2 called.')
        
class Child(parent1,parent2):             #parent1 is immediate parent class,parent2 is other.
    def __init__(self):
        print('__init__ of child called.')
        super().__init__()                  #calls the function of immediate parent class.
        parent2.__init__()                  #we can call the __init__ of the other class.
child = Child()

#METHOD RESOLUTION OBJECT gives the order in which classes are activated. 
print(Child.__mro__)                
