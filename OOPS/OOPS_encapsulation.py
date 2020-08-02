#encapsulation.
class unencapsulated:
    def __init__(self,rNo):
        
        self.roll_no = rNo
class encapsulated:
    def __init__(self,rNo):
        self.__roll_no = rNo

    def getRollNo(self) :
        return self.__roll_no
    
    def changeRollNo(self,no):
        self.__roll_no = no

unsafe = unencapsulated(1)

#prints the roll_no and thus  not private.
print('Printing a argument of an unencapsulated class.')
print(unsafe.roll_no)           

#easily modify and hence no integrity.
unsafe.roll_no = 2
print('Modifying and printing an argument of an unencapsulated class.')
print(unsafe.roll_no)

print('\n\n\n')

safe = encapsulated(1)                      # creating object of the class.
#cannot print an argument that is private.
try:
    print('Trying to print an argument of a encapsulated class.')
    print(safe.roll_no)                     # cannot access it.
except AttributeError:
    print('Fail:')
    print("-'encapsulated' object has no attribute 'roll_no' ")
    print('-i.e program cannot see if there is any argument named roll_no.')
    print('-Thus keeping it safe.')
    
#neither can modify it.
safe.__roll_no = 2
print('\n')
print('Even if we try to modify the argument, we wont be able to do it.')
print(safe.getRollNo())                     # prints the old value of roll_no not updated one.

print('\n')
safe.changeRollNo(3)
print('Succefully change the roll_no using changeRollNo function of the class.')
print(safe.getRollNo())
