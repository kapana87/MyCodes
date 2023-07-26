from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        self.birth_date = birth_date
        raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - 1
        age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
        return age

    @__init__.register(date)
    def for_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def for_str(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)

    @__init__.register(tuple)
    @__init__.register(list)
    def for_list(self, birth_date):
        self.birth_date = date(*birth_date)


errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]

for obj in errors:
    try:
        BirthInfo(obj)
    except TypeError as e:
        print(e)