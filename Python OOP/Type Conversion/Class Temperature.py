class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls(5 / 9 * (temperature - 32))

    def __str__(self):
        return f'{self.temperature.__round__(2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())

print()

t = Temperature.from_fahrenheit(-459.67)

print(t)
print(bool(t))
print(int(t))
print(f'{float(t):.2f}')
print(f'{t.to_fahrenheit():.2f}')