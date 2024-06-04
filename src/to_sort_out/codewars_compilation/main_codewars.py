from math import factorial


def print_numbers_in_line(n):
    for i in range(1, n + 1):
        print(i, end='')


def factorial_quotient(n):
    numerator = 0
    for i in range(1, n + 1):
        numerator += factorial(i)

    return int((numerator / factorial(n)) * (10 ** 6)) / 10 ** 6


def factorial_quotient_2(n):
    numerator = sum(factorial(i) for i in range(1, n + 1))
    return int((numerator / factorial(n)) * (10 ** 6)) / 10 ** 6


def my_factorial_1(m):
    fact = 1
    for i in range(2, m + 1):
        fact *= i
    return fact


def my_factorial_2(m):
    return 1 if (m == 0) else m * factorial(m - 1)


def main():
    res = factorial_quotient(2343)
    print(res)
    print(factorial_quotient_2(2343))
    print(my_factorial_1(10))
    print(my_factorial_2(10))


if __name__ == '__main__':
    main()
