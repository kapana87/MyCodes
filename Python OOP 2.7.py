from datetime import date
from functools import singledispatchmethod

class BirthInfo:
    def __init__(self, birth_date):
        self.birth_date = self._parse_birth_date(birth_date)

    @staticmethod
    def _parse_birth_date(birth_date):
        if isinstance(birth_date, date):
            return birth_date
        elif isinstance(birth_date, str):
            return date.fromisoformat(birth_date)
        elif isinstance(birth_date, (list, tuple)) and len(birth_date) == 3:
            return date(*birth_date)
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        return self._calculate_age(self.birth_date, date.today())

    @singledispatchmethod
    @staticmethod
    def _calculate_age(birth_date, today):
        raise NotImplementedError("Метод _calculate_age не реализован для данного типа данных")

    @_calculate_age.register
    @staticmethod
    def _calculate_age_date(birth_date: date, today: date):
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            return today.year - birth_date.year - 1
        return today.year - birth_date.year

    @_calculate_age.register
    @staticmethod
    def _calculate_age_str(birth_date: str, today: date):
        return BirthInfo._calculate_age_date(date.fromisoformat(birth_date), today)

    @_calculate_age.register
    @staticmethod
    def _calculate_age_list_tuple(birth_date: list, today: date):
        return BirthInfo._calculate_age_date(date(*birth_date), today)
