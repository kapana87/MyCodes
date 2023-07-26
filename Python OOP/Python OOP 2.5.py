from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    def neg(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @staticmethod
    @neg.register(int)
    @neg.register(float)
    def for_int_float(data):
        return -data

    @staticmethod
    @neg.register(bool)
    def for_bool(data):
        return not data


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))