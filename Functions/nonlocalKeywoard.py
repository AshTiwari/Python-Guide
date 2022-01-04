# nonlocal keywoard

def bindingFunc():
    nonBindingVar = 1
    bindingVar = 2
    
    def localFunc():
        nonlocal bindingVar
        bindingVar = 0

    localFunc()
    print(nonBindingVar)
    print(bindingVar)
    
if __name__ == "__main__":
    bindingFunc()
