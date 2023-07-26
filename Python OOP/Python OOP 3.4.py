class AnyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.kwargs = kwargs

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join(f"{key}={repr(value)}" for key, value in self.kwargs.items())}'

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join(f"{key}={repr(value)}" for key, value in self.kwargs.items())})'


obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))

attrs = {
    'name': 'Guido van Rossum',
    'birth_date': '31.01.1956',
    'age': 67,
    'career': 'python guru'
}
obj = AnyClass(**attrs)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)

attrs = {
    'name': 'Margaret Heafield Hamilton',
    'birth_date': '17.09.1936',
    'age': 86,
    'career': 'computer scientist'
}
obj = AnyClass(**attrs)
print(obj)