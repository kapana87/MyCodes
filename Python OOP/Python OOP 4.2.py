class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'ColoredPoint{self.x, self.y, self.color}'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(self.x * (-1), self.y * (-1), self.color)

    def __invert__(self):
        return ColoredPoint(self.y, self.x, tuple(255 - rgb for rgb in self.color))


point1 = ColoredPoint(1, 2, (100, 150, 200))
point2 = ~point1

print(repr(point1))
print(repr(point2))