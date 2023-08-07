class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr):
        if attr == 'total':
            self.total = self.price * self.quantity
        elif attr == 'name':
            return object.__getattribute__(self, attr).title()
        return object.__getattribute__(self, attr)


course = Item('pygen', 3900, 2)


print(course.name)
print(course.price)
print(course.quantity)
print(course.total)