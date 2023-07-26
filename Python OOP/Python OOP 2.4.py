from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    def process(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @staticmethod
    @process.register(float)
    @process.register(int)
    def for_int_float(data):
        return data * 2

    @staticmethod
    @process.register(str)
    def for_str(data):
        return data.upper()

    @staticmethod
    @process.register(list)
    def for_list(data):
        return sorted(data)

    @staticmethod
    @process.register(tuple)
    def for_tuple(data):
        return tuple(sorted(data))


try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)


print()

print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))

