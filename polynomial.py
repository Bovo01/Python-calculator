from __future__ import annotations
import fraction
import irrational


class polynomial:
    ''' CONSTRUCTOR '''

    def __init__(self, *args: int | fraction.fraction | irrational.irrational, **kwargs):
        self.numbers = []
        if not kwargs.get('ignoreChecks', False):
            self.__set_numbers(*args)
        else:
            self.numbers = list(args)

    ''' PRIVATE METHODS '''

    # Sets the numbers list adding all yuo can
    def __set_numbers(self, *args: int | fraction.fraction | irrational.irrational):
        ignored = []
        for i in range(len(args)):
            if i in ignored:
                continue
            n = args[i]
            if isinstance(n, int) or isinstance(n, fraction.fraction):
                if isinstance(n, int):
                    # Convert integer to fraction.fraction
                    n = fraction.fraction(n)

                # Sum all the integers and fraction.fractions together
                for j in range(i + 1, len(args)):
                    m = args[j]
                    if isinstance(m, int) or isinstance(m, fraction.fraction):
                        n += m
                        ignored.append(j)
                    elif isinstance(m, irrational.irrational) and m.rooted_part == 1:
                        n += m.int_part
                        ignored.append(j)
            elif isinstance(n, irrational.irrational):
                # Sum all the irrational.irrationals together
                for j in range(i + 1, len(args)):
                    m = args[j]
                    if isinstance(m, irrational.irrational) and m.rooted_part == n.rooted_part:
                        n += m
                        ignored.append(j)
            if n != 0:
                self.numbers.append(n)

        if len(self.numbers) == 0:
            self.numbers.append(fraction.fraction(0))

    # If the polynomial contains only one element, it returns it
    def reduce(self) -> polynomial | fraction.fraction | irrational.irrational | int:
        if len(self.numbers) == 0:
            return 0
        elif len(self.numbers) == 1:
            return self.numbers[0]
        else:
            return self

    ''' TO STRING METHOD '''

    def __str__(self) -> str:
        s = '('
        for n in self.numbers:
            if s != '(':
                if n < 0:
                    s += ' - '
                    n = -n
                else:
                    s += ' + '
            s += str(n)
        s += ')'
        return s

    ''' CALCULATIONS METHODS '''

    # Overload binary operator +
    def __add__(self, other: int | fraction.fraction | irrational.irrational | polynomial) -> int | fraction.fraction | irrational.irrational | polynomial:
        numbers = list(self.numbers)
        if not isinstance(other, polynomial):
            found = False
            # Sum for integers, fractions and irrational numbers
            for i in range(len(numbers)):
                n = numbers[i]
                sum = n + other
                if not isinstance(sum, polynomial):
                    if sum == 0:
                        del numbers[i]
                    else:
                        numbers[i] = sum
                    found = True
                    break
            if not found:
                numbers.append(other)
        else:
            i = 0
            added = []
            while i < len(numbers):  # Sum of two polynomials
                n = numbers[i]
                for j in range(len(other.numbers)):
                    m = other.numbers[j]
                    sum = n + m
                    if not isinstance(sum, polynomial):
                        if sum == 0:
                            del numbers[i]
                        else:
                            numbers[i] = sum
                            i += 1
                        added.append(j)
                        break
            for j in range(len(other.numbers)):
                if j not in added:
                    numbers.append(other.numbers[j])

        return polynomial(*numbers).reduce()

    # Overload unary operator -
    def __neg__(self) -> int | fraction.fraction | irrational.irrational | polynomial:
        return polynomial(*(-n for n in self.numbers)).reduce()

    # Overload binary operator -
    def __sub__(self, other: int | fraction.fraction | irrational.irrational | polynomial) -> int | fraction.fraction | irrational.irrational | polynomial:
        return self + -other

    def __mul__(self, other: int | fraction.fraction | irrational.irrational | polynomial) -> int | fraction.fraction | irrational.irrational | polynomial:
        if not isinstance(other, polynomial):
            pass  # TODO

    ''' COMPARISON METHODS '''
    # TODO if necessary: Overload binary operator ==, !=, <
