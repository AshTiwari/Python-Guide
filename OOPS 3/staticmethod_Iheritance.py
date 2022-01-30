# static method in inheritance

class Parent:
    class_var1 = 1

    def __init__(self):
        self.param1 = 10
        self.param2 = Parent.staticmethod1()
        self.param3 = self.staticmethod2()

    @staticmethod
    def staticmethod1():
         return 20
    @staticmethod
    def staticmethod2():
        return 30

class child(Parent):
    @staticmethod
    def staticmethod1():
         return 200
    @staticmethod
    def staticmethod2():
        return 300


if __name__ == "__main__":
    object1 = child()
    print(object1.param2)
    print(object1.param3)


    
