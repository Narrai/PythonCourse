"""
    File: rational.py
    Resources to manipulate rational numbers.
"""


class Rational(object):
    """Represents a rational number."""

    def __init__(self, numer, denom):
        """Constructor creates a number with the given numerator and denominator
            and reduces it to lowest terms.
        """
        self._numer = numer
        self._denom = denom
        self._reduce()

    def numerator(self):
        """Returns the numerator"""
        return self._numer

    # numer = property(numerator)

    def denominator(self):
        """Returns the denominator"""
        return self._denom

    # denom = property(denominator)

    def __str__(self):
        """Returns the string representation of the number."""
        return str(self._numer) + "/" + str(self._denom)

    def _reduce(self):
        """Helper to reduce the number to lowest terms."""
        divisor = self._gcd(self._numer, self._denom)
        self._numer = self._numer // divisor
        self._denom = self._denom // divisor

    def _gcd(self, a, b):
        """Euclid's algorithm for the creates common divisor."""
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    # Methods for arithmetic  and comparisons go here
    def __add__(self, other):
        """Returns the sum of the numbers."""
        newNumer = self._numer * other._denom + \
                   other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumer, newDenom)

    def __lt__(self, other):
        """Returns self < other."""
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes < means

    def __eq__(self, other):
        """Tests self and other for equality"""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self._numer == other._numer and self._denom == other._denom

    def __mul__(self, other):
        """Returns the product of two rational numbers"""
        n1 = self._numer * other._numer
        n2 = self._denom * other._denom
        return Rational(n1, n2)

if __name__ == "__main__":
    # r = Rational(2, 5)
    r1 = Rational(7, 35)
    # print(r + r1)
    # r.__lt__(r1)
    # print(r < r1)
    # print(r * r1)
    # print(r.__eq__(r1))
    print(r1)

















