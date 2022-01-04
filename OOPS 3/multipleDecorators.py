# multiple decorators.

from time import time

def cache(func):
    cached_data = {}
    def cached(*args):
        if cached_data.get(args, None):
            print("Returning Cached Data.")
            return cached_data[args]
        else:
            print("Caching Data.")
            cached_data[args] = func(*args)
            return cached_data[args]
    return cached

def exeTime(func):
    def timeFun(*args):
        before = time()
        ret = func(*args)
        after = time()
        print(f"Execution time: {after-before}")
        return ret
    return timeFun

def trace(func):
    def traceFun(*args):
        print(f"Calling function: {func}")
        return func(*args)
    return traceFun

@exeTime
@cache
@trace
def add(x,y):
    return x+y

@exeTime
@cache
@trace
def sub(x,y):
    return x-y

if __name__ == "__main__":
    print(add(3,5))
    print(add(3,5))
    print(sub(5,3))
    print(sub(5,3))
    



        
