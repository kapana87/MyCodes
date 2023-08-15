class ColoredPoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @property
    def x_getter(self):
        return self.x

    @property
    def y_getter(self):
        return self.y

    @property
    def color_getter(self):
        return self.color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError
        object.__setattr__(self, key, value)


point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))

print()

points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)

print()

point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')