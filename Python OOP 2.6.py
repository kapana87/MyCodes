from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    def format(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @staticmethod
    @format.register(int)
    @format.register(float)
    def for_int_float(data):
        if isinstance(data, int):
            print(f'Целое число: {data}')
        else:
            print(f'Вещественное число: {data}')

    @staticmethod
    @format.register(list)
    @format.register(tuple)
    def for_list_tuple(data):
        if isinstance(data, list):
            print(f'Элементы списка: {", ".join(map(str, data))}')
        else:
            print(f'Элементы кортежа: {", ".join(map(str, data))}')

    @staticmethod
    @format.register(dict)
    def for_dict(data):
        print(f'Пары словаря: {", ".join(map(str, data.items()))}')


Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

print()

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))