from functools import reduce


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


def main():
    number = 7
    factorial = calculate_factorial(number)
    print(factorial)

    rec_fact = recursive_factorial(number)
    print(rec_fact)

    print(factorial_with_reduce(5))


if __name__ == '__main__':
    main()
