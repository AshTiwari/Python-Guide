# factory functions
# uses concept of closures.

# factory function
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp)
    return raise_to_exp

if __name__ == "__main__":
    square = raise_to(2)
    print(square(1))
    print(square(25))
    cube = raise_to(3)
    print(cube(1))
    print(cube(25))
