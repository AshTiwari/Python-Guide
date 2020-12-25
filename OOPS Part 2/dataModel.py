#data model | Double Underscore function |Dunder methods |
#protocol view of python.

#some behaviour I want to implement -> write __fucntion__
#pattern that we observe:
# for some top level function or top-level syntax -> there is a corresponding. __fucntion.
# for x+y -> __add__
# for initializing x -> __init__
# for representation -> __repr__
# for x() -> __call__

class polynomial:
    def __init__(self,*coefficients):
        self.coefficients = coefficients
        
    #change the default repr (representation) function of python.
    #trigerred when an object is printed.
    def __repr__(self):
        return 'polynomial(*{})'.format(self.coefficients)

    #triggerd when two objects are added using + sign.
    def __add__(self,other):
        return polynomial(*(x+y for x,y in zip(self.coefficients, other.coefficients)))

        
p1 = polynomial(1,2,3)    #triggers __init__
p2 = polynomial(4,5,6)

print(p1)           #triggers __repr__
print(p2)           
print(p1+p2)        #triggers __add__
