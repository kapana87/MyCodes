from math import pow, sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        discriminant = pow(self.b, 2) - 4 * self.a * self.c
        if discriminant >= 0:
            return (-self.b - sqrt(discriminant)) / (2 * self.a)
        else:
            return None

    @property
    def x2(self):
        discriminant = pow(self.b, 2) - 4 * self.a * self.c
        if discriminant >= 0:
            return (-self.b + sqrt(discriminant)) / (2 * self.a)
        else:
            return None

    @property
    def view(self):
        pattern1 = '{}x^2'.format(abs(self.a)) if self.a > 0 else '-{}x^2'.format(abs(self.a))
        pattern2 = ' + {}x'.format(self.b) if self.b >= 0 else ' - {}x'.format(abs(self.b))
        pattern3 = ' + {}'.format(self.c) if self.c >= 0 else ' - {}'.format(abs(self.c))
        return pattern1 + pattern2 +pattern3

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, trinomial_coefficients):
        self.a, self.b, self.c = trinomial_coefficients


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

print()

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)
