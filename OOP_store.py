# OOP

class Item():
    def __init__(self, name: str, price: float, quantity=0):
        # argument validation
        #assert price >= 0
        #assert quantity >= 0
        # assign attributes to object
        self.name = name
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    mobile = Item('Mobile', '1000', 10)
    laptop = Item('Laptop', 10000, 5)
