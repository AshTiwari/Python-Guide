# self


class Class():
    def func(self):
        return self

if __name__ == '__main__':
    obj = Class()
    if obj == obj.func():
        print("First argument in method is always the object.")
