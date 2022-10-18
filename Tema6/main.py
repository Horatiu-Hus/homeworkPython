import math


class Fraction:
    def __init__(self, numerator, denominator):
        try:
            numerator = int(numerator)
        except ValueError:
            raise ValueError('Numerator should be int')

        try:
            denominator = int(denominator)
        except ValueError:
            raise ValueError('Denominator should be int')

        if denominator == 0:
            raise ValueError('Denominator cannot be 0')

        self._numerator, self._denominator = self._get_simplified(numerator, denominator)

    @staticmethod
    def _get_simplified(numerator, denominator):
        gcd = math.gcd(numerator, denominator)  # Greatest Common Divisor
        print('gcd', gcd)

        return numerator // gcd, denominator // gcd

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def __add__(self, other):
        lcm = math.lcm(self._denominator, other.denominator)    # Lowest Common Multiple
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator + second_fraction_numerator, lcm)

    def __sub__(self, other):
        lcm = math.lcm(self._denominator, other.denominator)
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator - second_fraction_numerator, lcm)

    def inverse(self):
        return Fraction(self._denominator, self._numerator)


if __name__ == '__main__':

    x = Fraction(2, 4)
    y = Fraction(3, 8)
    z = x + y

    print('z', z)

    x2 = Fraction(6, 4)
    y2 = Fraction(4, 8)
    z2 = x2 - y2

    print('z2', z2)
