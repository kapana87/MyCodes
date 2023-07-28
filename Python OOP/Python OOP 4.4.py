class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo{self.proteins, self.fats, self.carbohydrates}'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented


food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)

food1 = FoodInfo(10, 20, 30)

try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')

print()

pfc = [(751.26, 778.77, 947.51), (597.41, 508.5, 532.96), (800.55, 617.5, 525.14), (741.99, 785.53, 664.71),
       (525.69, 892.41, 541.41), (888.8, 802.56, 868.78), (609.65, 855.43, 949.44), (705.25, 592.28, 738.72),
       (514.88, 617.22, 557.5), (948.62, 938.7, 817.17), (783.98, 628.32, 686.38), (894.9, 815.81, 715.19),
       (586.79, 826.68, 637.5), (670.53, 683.69, 841.56), (583.9, 607.34, 853.35), (954.67, 950.76, 822.19),
       (718.94, 658.12, 537.2), (556.53, 686.17, 622.61), (699.8, 872.49, 908.3), (622.3, 920.97, 801.17)]

FoodInfo.__round__ = lambda instance: FoodInfo(
    round(instance.proteins, 2),
    round(instance.fats, 2),
    round(instance.carbohydrates, 2)
)

food1 = FoodInfo(1000, 2000, 3000)
for p, f, c in pfc:
    food2 = FoodInfo(p, f, c)
    add = food1 + food2
    mul = food1 * p
    truediv = food1 // c
    print(round(add), round(mul), round(truediv))

print()

food = FoodInfo(10, 20, 30)
print(food.__add__([]))
print(food.__mul__(()))
print(food.__truediv__({}))
print(food.__floordiv__(set()))