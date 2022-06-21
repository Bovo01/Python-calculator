from __future__ import annotations
from math import gcd

import irrational
import polynomial


class fraction:
    ''' CONSTRUCTOR '''

    def __init__(self, numerator: int | irrational.irrational, denominator: int | irrational.irrational = 1):
        if denominator == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        self.numerator = numerator
        self.denominator = denominator
        self.__check_valid_params()
        self.__minimize()

    ''' PRIVATE METHODS '''

    # Checks that the numerator and denominator are valid types
    def __check_valid_params(self):
        if not isinstance(self.numerator, int) and not isinstance(self.numerator, fraction) and not isinstance(self.numerator, irrational.irrational):
            raise TypeError(f'Invalid numerator type {type(self.numerator)}')
        if not isinstance(self.denominator, int) and not isinstance(self.denominator, fraction) and not isinstance(self.denominator, irrational.irrational):
            raise TypeError(
                f'Invalid denominator type {type(self.denominator)}')

    # Minimizes the fraction to the lowest terms and removes roots from the denominator
    def __minimize(self) -> None:
        # Change sign
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        # Reduce fraction
        if isinstance(self.numerator, int) and isinstance(self.denominator, int):
            MCD = gcd(self.numerator, self.denominator)
            self.numerator //= MCD
            self.denominator //= MCD
        elif isinstance(self.denominator, int):
            MCD = gcd(self.numerator.int_part, self.denominator)
            self.numerator.int_part //= MCD
            self.denominator //= MCD
        elif isinstance(self.denominator, irrational.irrational):
            # Remove the irrational part from the denominator
            i = irrational.irrational(self.denominator.rooted_part)
            self.denominator = i * self.denominator
            self.numerator = i * self.numerator
            # gcd of the numerator and denominator int parts
            MCD = gcd(self.numerator.int_part, self.denominator.int_part)
            self.numerator.int_part //= MCD
            self.denominator.int_part //= MCD

    ''' TO STRING METHOD '''

    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f'{self.numerator}/{self.denominator}'

    ''' CALCULATIONS METHODS '''

    # Overload binary operator +
    def __add__(self, other: fraction | int | irrational.irrational | polynomial.polynomial) -> fraction | polynomial.polynomial:
        if isinstance(other, int):
            other = fraction(other)
        if isinstance(other, fraction):
            if isinstance(self.denominator, int) and isinstance(other.denominator, int):
                return fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
            elif isinstance(self.numerator, irrational.irrational) and isinstance(other.numerator, irrational.irrational) and self.numerator.rooted_part == other.numerator.rooted_part:
                return fraction(irrational.irrational(self.numerator.rooted_part, self.numerator.int_part * other.denominator + other.numerator.int_part * self.denominator), self.denominator * other.denominator)
            else:
                return polynomial.polynomial(self, other, ignoreChecks=True)
        elif isinstance(other, irrational.irrational):
            if isinstance(self.numerator, irrational.irrational) and self.numerator.rooted_part == other.rooted_part:
                return fraction(self.numerator + other * self.denominator, self.denominator)
            else:
                return polynomial.polynomial(self, other, ignoreChecks=True)
        elif isinstance(other, polynomial.polynomial):
            return other + self

    # Overload unary operator -
    def __neg__(self) -> fraction:
        return fraction(-self.numerator, self.denominator)

    # Overload binary operator -
    def __sub__(self, other: fraction | int | irrational.irrational | polynomial.polynomial) -> fraction | polynomial.polynomial:
        return self + -other

    # Overload binary operator *
    def __mul__(self, other: fraction | int | irrational.irrational) -> fraction:
        if isinstance(other, fraction):
            if isinstance(self.numerator, irrational.irrational) or isinstance(other.numerator, irrational.irrational):
                # Order must be (irrational * irrational) or (irrational * int) but not (int * irrational)
                if isinstance(self.numerator, irrational.irrational):
                    return fraction(self.numerator * other.numerator, self.denominator * other.denominator)
                else:
                    return fraction(other.numerator * self.numerator, self.denominator * other.denominator)
            else:
                return fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return fraction(self.numerator * other, self.denominator)
        elif isinstance(other, irrational.irrational):
            return fraction(other.numerator * self.numerator, self.denominator)

    # Returns the reciprocal of this fraction
    def reciprocal(self):
        return fraction(self.denominator, self.numerator)

    # Overload binary operator /
    def __truediv__(self, other: fraction | int) -> fraction:
        return self * other.reciprocal()

    # Overload binary operator //
    def __floordiv__(self, other: fraction | int) -> fraction:
        return self / other

    ''' COMPARISON METHODS '''
    # Overload binary operator ==

    def __eq__(self, other: fraction | int | irrational.irrational) -> bool:
        if isinstance(other, fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other and self.denominator == 1
        elif isinstance(other, irrational.irrational):
            return self.numerator == other.int_part and self.denominator == other.rooted_part == 1

    # Overload binary operator !=
    def __ne__(self, other: fraction | int | irrational.irrational) -> bool:
        return not self == other

    # Overload binary operator <
    def __lt__(self, other: int | fraction) -> bool:
        if isinstance(other, fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
