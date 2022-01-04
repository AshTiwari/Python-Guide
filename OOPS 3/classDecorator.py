# decorators with class

class decorator:
    def __init__(self,func):
        self.func = func

    def __call__(self,*args):
        print(self.func(*args))

@decorator
def add(x,y):
    return(x+y)

if __name__ == "__main__":
    add(2,3)
    add(3,4)
