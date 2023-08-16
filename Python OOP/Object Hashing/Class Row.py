class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'Row({", ".join(f"{key}={repr(value)}" for key, value in self.__dict__.items())})'

    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Row):
            return not self.__eq__(other)
        return NotImplemented

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError('Установка нового атрибута невозможна')
        elif key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __hash__(self):
        # Сгенерируем хеш на основе словаря атрибутов
        return hash(tuple(self.__dict__.items()))


row = Row(a='A', b='B', c='C')

print(row)
print(row.a, row.b, row.c)

print()

row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)

row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print()

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))

print()

row = Row(a=1, b=2, c=3)

try:
    del row.a
except AttributeError as e:
    print(e)

print()

row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)

print()

row = Row(a=1, b=2, c=3)

try:
    row.a = 10
except AttributeError as e:
    print(e)