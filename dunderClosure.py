# dunder closure

def outerFunc():
    var1 = 1
    var2 = 2
    def innerFunc():
        var3 = var1 + var2
        return var3
    return innerFunc

if __name__== "__main__":
    ifunc = outerFunc()
    print(ifunc())
    # __closure__ return tuple of objects of outerFunc.
    print(ifunc.__closure__)
