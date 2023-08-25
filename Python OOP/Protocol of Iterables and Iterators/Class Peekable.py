from copy import deepcopy


class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def peek(self, default=StopIteration):
        iterable = list(deepcopy(self.iterable))
        if iterable:
            return iterable[0]
        elif default != StopIteration:
            return default
        else:
            raise default

    def __iter__(self):
        yield from self.iterable

    def __next__(self):
        try:
            return next(self.iterable)
        except StopIteration:
            raise StopIteration


iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)

print()

iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

print()

iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))

print()

# TEST_4:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')

print()

iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))