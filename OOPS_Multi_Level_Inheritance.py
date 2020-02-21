# multiple inheritance

class parent:
    def __init__(self):
        print('__init__ of parent class.')

class son(parent):
    def __init__(self):
        print('__init__ of son.')

class daughter(parent):
    def __init__(self):
        print('__init__ of daughter.')

class grandchild(daughter,son):
    pass

parent()
son()
daughter()

gchild = grandchild()       # calls the first parent.



    
