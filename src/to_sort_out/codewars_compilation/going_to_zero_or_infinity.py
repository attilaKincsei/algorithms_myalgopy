from math import factorial
from time import time


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


_FACTORIAL_TABLE = [1, 1]


def fast_factorial(n):
    """
    http://code.activestate.com/recipes/577241-faster-factorial/
    :return:
    """
    if n < len(_FACTORIAL_TABLE):
        return _FACTORIAL_TABLE[n]

    last_index = len(_FACTORIAL_TABLE) - 1
    highest_total = _FACTORIAL_TABLE[last_index]
    for i in range(last_index + 1, n + 1):
        highest_total *= i
        _FACTORIAL_TABLE.append(highest_total)
    return highest_total


def going(n):
    """
    codewars solution with recursion
    :param n: non-negative integer
    :return: (1 / n!) * (1! + 2! + 3! + ... + n!) [truncated to 6 decimal places]
    """

    def factorial(m):
        return 1 if (m == 0) else m * factorial(m - 1)

    numerator = sum(factorial(i) for i in range(1, n + 1))
    return int((numerator / factorial(n)) * (10 ** 6)) / 10 ** 6


def going_best(n):
    """
    best solution on codewars
    :param n:
    :return:
    """
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
    return int(s * 1e6) / 1e6

def main():
    n = 1000
    # print(my_factorial_1(n))
    # print(my_factorial_2(n))
    start = time() * 1000
    res = fast_factorial(n)
    end = time() * 1000
    print("Result: {0}\nTime in ms: {1}".format(res, end - start))


if __name__ == '__main__':
    main()
