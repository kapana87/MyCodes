class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        return self.roman_to_int(self.number)

    def roman_to_int(self, roman):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        decimal = 0
        prev_value = 0

        for char in reversed(roman):
            value = values[char]
            if value < prev_value:
                decimal -= value
            else:
                decimal += value
                prev_value = value

        return decimal

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_int(self.number) == self.roman_to_int(other.number)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_int(other.number) != self.roman_to_int(self.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_int(self.number) < self.roman_to_int(other.number)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_int(self.number) <= self.roman_to_int(other.number)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_int(self.number) > self.roman_to_int(other.number)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_int(self.number) >= self.roman_to_int(other.number)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            decimal_sum = self.roman_to_int(self.number) + self.roman_to_int(other.number)
            return RomanNumeral(self.int_to_roman(decimal_sum))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            decimal_diff = self.roman_to_int(self.number) - self.roman_to_int(other.number)
            return RomanNumeral(self.int_to_roman(decimal_diff))
        return NotImplemented

    def int_to_roman(self, decimal):
        val_to_roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        roman = ""

        for val in sorted(val_to_roman.keys(), reverse=True):
            while decimal >= val:
                roman += val_to_roman[val]
                decimal -= val

        return roman


# TEST_8:
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

print()

# TEST_9:
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))