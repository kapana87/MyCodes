from datetime import datetime, date


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, dates):
        pattern = {'us': '%m-%d-%Y', 'ru': '%d.%m.%Y', 'ca': '%Y-%m-%d',
                   'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
        return datetime.strftime(dates, pattern[self.country_code])


ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))

print()

us_format = DateFormatter('us')

print(us_format(date(2022, 11, 7)))

print()

ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))

print()

fr_format = DateFormatter('fr')

print(fr_format(date(2022, 11, 7)))