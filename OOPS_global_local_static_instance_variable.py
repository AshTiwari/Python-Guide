#global, local, static, instance variable.

#global variable are defined at the op of program or defined using keyword:global

global global_var1 = 1

def local_variable:
    #local variable are defined inside of a function or a class.
    local_var1 = 2


class static_instance:
    #local variable are defined inside of a function or a class.
    local_var2 = 3


    def __init__(self):
        #all variables defined in the function of a class.
        self.static_var1 = 4

    def static(self):
        self.static_var2 = 5

    local_var3 = 6




    
