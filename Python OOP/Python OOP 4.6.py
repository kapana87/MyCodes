def check_type(*arg_types):
    def decorator(func):
        def wrapped(self, other, *args, **kwargs):
            if isinstance(other, arg_types):
                return func(self, other, *args, **kwargs)
            return NotImplemented
        return wrapped
    return decorator


class PSuperString:
    pass


class SuperString(PSuperString):

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string}'

    @check_type(PSuperString)
    def __add__(self, other):
        return SuperString(self.string + other.string)

    @check_type(int, float)
    def __mul__(self, other):
        return SuperString(self.string * other)

    @check_type(int, float)
    def __rmul__(self, other):
        return self.__mul__(other)

    @check_type(int, float)
    def __truediv__(self, other):
        return SuperString(self.string[:int(len(self.string) / other)])

    @check_type(int)
    def __lshift__(self, other):
        if other >= len(self.string):
            return SuperString("")
        elif other == 0:
            return SuperString(self.string)
        return SuperString(self.string[:-other])

    @check_type(int)
    def __rshift__(self, other):
        if other >= len(self.string):
            return SuperString("")
        elif other == 0:
            return SuperString(self.string)
        return SuperString(self.string[other:])


s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)

print()

s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

print()

s = SuperString('beegeek')

print(s << 4)
print(s >> 3)

print()

s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

print()

superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))

print()

s = SuperString('beegeek')
for i in range(9):
    print(f'{s} >> {i} =', s >> i)