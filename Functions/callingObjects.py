# calling an object of class.

class Class:
    def __call__(self):
        print("Object is called.")

object1 = Class()
object1()
object1.__call__()
        
