# cashhing with decorators.

class classDecorator:
    def __init__(self,func):
        self.func = func
        self.cached_data = {}
        
    def __call__(self,*args):
        if self.cached_data.get(args, None):
            ret = self.cached_data[args]
            print("Data is retrived from cache.")
        else:
            ret = self.func(*args)
            self.cached_data[args] = ret
            print("Data is cached.")
        print(self.cached_data)  
        return ret
    
@classDecorator
def add(x,y):
    return x+y

if __name__ == "__main__":
    print(add(2,3))
    print(add(-5,2))
    print(add(2,3))
    print(add(-5,2))
