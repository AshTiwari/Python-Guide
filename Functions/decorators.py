# decorators

from time import time

# decorator function
def exeTime(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        executionTime = after - before
        print(f"Execution Time: {executionTime}")
        return rv
    return f

@exeTime
def add(x,y):
    print(x+y)

@exeTime
def sub(x,y):
    print(x-y)

if __name__ == "__main__":
    # decorator method
    add(3,5)
    add(5,6)
    sub(5,3)
    sub(6,5)

    # non decorator method
    addFunc = exeTime(add)
    addFunc(3,5)
    addFunc(5,6)
    subFunc = exeTime(sub)
    subFunc(5,3)
    subFunc(6,5)
