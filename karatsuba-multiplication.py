def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y))) // 2

        xl = x // 10 ** m
        xr = x % 10 ** m
        yl = y // 10 ** m
        yr = y % 10 ** m

        f0 = karatsuba(xr, yr)
        f1 = karatsuba((xl + xr), (yl + yr))
        f2 = karatsuba(xl, yl)

        return (f2 * 10**(2 * m)) + ((f1 - f2 - f0) * 10 ** m) + f0


def main():
    x, y = map(int, input().split())

    print(karatsuba(x, y))


if __name__ == '__main__':
    main()
