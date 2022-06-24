from fraction import fraction
from irrational import irrational
from polynomial import polynomial


def main():
    rational_test()
    irrational_test()
    polynomial_test()
    mixed_test()


def rational_test():
    f1 = fraction(1, 2)
    f2 = fraction(2, 5)

    print('\n-----RATIONAL TEST-----')
    print(f'f1: {f1}')
    print(f'f2: {f2}')
    print(f'f1 + f2: {f1 + f2}')
    print(f'f1 - f2: {f1 - f2}')
    print(f'f1 * f2: {f1 * f2}')
    print(f'f1 / f2: {f1 / f2}')
    print(f'f1 + 2: {f1 + 2}')
    print(f'f1 * 2: {f1 * 2}')
    print(f'type(f1 * 2): {type(f1 * 2)}')
    print(f'f1 / 2: {f1 / 2}')
    print(f'-f1: {-f1}')
    print(f'-f2: {-f2}')


def irrational_test():
    i1 = irrational(75)
    i2 = irrational(12)

    print('\n-----IRRATIONAL TEST-----')
    print(f'i1: {i1}')
    print(f'i2: {i2}')
    print(f'i1 + i2: {i1 + i2}')
    print(f'i1 - i2: {i1 - i2}')
    print(f'i1 * i2: {i1 * i2}')

    fi = fraction(1, irrational(2))
    f = fraction(1, 2)
    i3 = irrational(8)
    print(f'fi: {fi}')
    print(f'f: {f}')
    print(f'i3: {i3}')
    print(f'fi + f: {fi + f}')
    print(f'fi + i3: {fi + i3}')


def polynomial_test():
    p1 = polynomial(fraction(2,3), 2, irrational(12), irrational(4))
    p2 = polynomial(1, 2, 3, irrational(12))

    print('\n-----POLYNOMIAL TEST-----')
    print(f'p1: {p1}')
    print(f'p2: {p2}')
    print(f'p1 + 1/2: {p1 + fraction(1,2)}')
    print(f'p1 + p2: {p1 + p2}')
    print(f'p1 - p2: {p1 - p2}')
    print(f'p1 - p1: {p1 - p1}')
    print(f'p1 * 3: {p1 * 3}')
    print(f'p1 * p2: {p1 * p2}')
    print(f'p2 * p1: {p2 * p1}')
    print(f'p1 / 3: {p1 / 3}')
    

def mixed_test():
    f = fraction(1, 2)
    i = irrational(2)

    print('\n-----MIXED TEST-----')
    print(f'f: {f}')
    print(f'i: {i}')
    print(f'f + i: {f + i}')
    print(f'f - i: {f - i}')

    fi = fraction(1, irrational(2))
    print(f'fi: {fi}')
    print(f'fi + i: {fi + i}')

if __name__ == "__main__":
    main()
