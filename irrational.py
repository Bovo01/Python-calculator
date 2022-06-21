from __future__ import annotations
from math import sqrt

import fraction
import polynomial


class irrational:
    ''' CONSTRUCTOR '''
    def __init__(self, rooted_part: int, int_part: int = 1):
        self.rooted_part = rooted_part
        self.int_part = int_part
        if self.rooted_part < 0:
            raise ValueError('Rooted part must be positive')
        self.__minimize()

    def __minimize(self):
        if self.int_part == 0:
            self.rooted_part = 1
        if self.rooted_part == 0:
            self.rooted_part = 1
            self.int_part = 0
            return
        ROOT_INDEX = 2
        i = 2
        while i**ROOT_INDEX <= self.rooted_part:
            if self.rooted_part % i**ROOT_INDEX == 0:
                self.rooted_part //= i**ROOT_INDEX
                self.int_part *= i
            else:
                i += 1

    ''' TO STRING METHOD '''

    def __str__(self) -> str:
        if self.rooted_part == 1:
            return f'{self.int_part}'
        elif self.int_part == 0:
            return '0'
        elif self.int_part == 1:
            return f'\u221A{self.rooted_part}'
        elif self.int_part == -1:
            return f'-\u221A{self.rooted_part}'
        else:
            return f'{self.int_part}\u221A{self.rooted_part}'

    ''' CALCULATIONS METHODS '''

    # Overload binary operator +
    def __add__(self, other: irrational | int | fraction.fraction) -> irrational | polynomial.polynomial | int:
        if isinstance(other, irrational):
            if self.rooted_part == other.rooted_part:
                return irrational(self.rooted_part, self.int_part + other.int_part)
            else:
                return polynomial.polynomial(self, other, ignoreChecks=True)
        elif isinstance(other, int):
            if self.rooted_part == 1:
                return self.int_part + other
            else:
                return polynomial.polynomial(self, other, ignoreChecks=True)
        elif isinstance(other, fraction.fraction):
            return other + self

    # Overload unary operator -
    def __neg__(self) -> irrational:
        return irrational(self.rooted_part, -self.int_part)

    # Overload binary operator -
    def __sub__(self, other: irrational) -> irrational:
        if self.rooted_part == other.rooted_part:
            return self + -other
        else:
            raise ValueError('Cannot sub irrationals with different roots')

    # Overload binary operator *
    def __mul__(self, other: irrational | int) -> irrational:
        if isinstance(other, irrational):
            return irrational(self.rooted_part * other.rooted_part, self.int_part * other.int_part)
        elif isinstance(other, int):
            return irrational(self.rooted_part, self.int_part * other)

    # Overload binary operator /
    def __truediv__(self, other: irrational) -> irrational:
        raise RuntimeError('Unimplemented')

    # Overload binary operator //
    def __floordiv__(self, other: irrational) -> irrational:
        return self.__truediv__(self, other)

    ''' COMPARISON METHODS '''
    # Overload binary operator ==

    def __eq__(self, other: irrational | int | fraction.fraction) -> bool:
        if isinstance(other, irrational):
            return self.rooted_part == other.rooted_part and self.int_part == other.int_part
        elif isinstance(other, int):
            return self.int_part == other and self.rooted_part == 1
        elif isinstance(other, fraction.fraction):
            return other.denominator == self.rooted_part == 1 and self.int_part == other.numerator

    # Overload binary operator !=
    def __ne__(self, other: irrational | int | fraction.fraction) -> bool:
        return not self == other

    # Overload binary operator <
    def __lt__(self, other: int | irrational) -> bool:
        if isinstance(other, int):
            return self.int_part * sqrt(self.rooted_part) < other
        elif isinstance(other, irrational):
            if self.rooted_part == other.rooted_part:
                return self.int_part < other.int_part
            else:
                return self.int_part * sqrt(other.rooted_part) < other.int_part * sqrt(self.rooted_part)
