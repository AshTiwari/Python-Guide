# cashhing with decorators.

def cached(func):
    cached_data = {}
    
    def cacheFunc(*args):
        if cached_data.get(args, None):
            ret = cached_data[args]
            print("Data is retrived from cache.")
        else:
            ret = func(*args)
            cached_data[args] = ret
            print("Data is cached.")
        print(cached_data)  
        return ret
    return cacheFunc

@cached
def add(x,y):
    return x+y

if __name__ == "__main__":
    print(add(2,3))
    print(add(-5,2))
    print(add(2,3))
    print(add(-5,2))
