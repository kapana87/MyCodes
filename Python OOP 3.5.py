class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y}'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.x != other.x or self.y != other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x != other[0] or self.y != other[1]
        return NotImplemented


a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)

print()

vector = Vector(0, 1)

print(vector.__eq__(1))
print(vector.__ne__(1.1))
print(vector.__gt__(range(5)))
print(vector.__lt__([1, 2, 3]))
print(vector.__ge__({4, 5, 6}))
print(vector.__le__({1: 'one'}))

print()

vectors1 = [Vector(114, 220), Vector(180, 148), Vector(85, 58), Vector(49, 246), Vector(110, 250), Vector(50, 91), Vector(60, 55), Vector(75, 238), Vector(189, 88), Vector(33, 190)]
vectors2 = [Vector(148, 144), Vector(169, 296), Vector(85, 58), Vector(172, 94), Vector(191, 55), Vector(50, 91), Vector(181, 150), Vector(43, 167), Vector(98, 238), Vector(33, 190)]

for v1, v2 in zip(vectors1, vectors2):
    print(v1 == v2, v1 != v2)