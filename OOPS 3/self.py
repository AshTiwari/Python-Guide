# self keyword in Class

class Class:
    def __int__(self):
        print(0)
    def method1(self1):
        print(1)
    def method2(self2):
        self2.method1()
        print(2)

object1 = Class()
object1.method1()
object1.method2()
