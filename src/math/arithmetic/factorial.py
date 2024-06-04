from functools import reduce


def factorial_recursive(x):
    if x == 1:
        return 1
    else:
        return x * factorial_recursive(x - 1)


def calculate_factorial(n):
    if n < 0:
        raise ArithmeticError
    if n < 2:
        return n
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


def recursive_factorial(n):
    if n < 0: raise ArithmeticError
    if n == 0: return 1
    if n == 1: return n
    return n * recursive_factorial(n - 1)


def factorial_with_reduce(n):
    return reduce(lambda x, y: x * y, range(2, n + 1))



