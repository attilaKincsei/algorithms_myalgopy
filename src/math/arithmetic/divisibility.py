from random import randint

# prime number generator (sieve of Eratosthenes)
# greatest common divisor (Euclid's algorithm)
# get prime divisors
# lowest common denominator
# lowest common multiple


# Check if integer is prime by finding divisors
def divides(a, b):
    return b % a == 0


def find_divisor(n, test_divisor):
    if test_divisor ** 2 > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, 3 if test_divisor == 2 else test_divisor + 2)


def smallest_divisor(n):
    return find_divisor(n, 2)


def prime(n):
    return n == smallest_divisor(n)


"""
Checking primality using Fermat's little theorem
O(log n) time complexity
"""


def expmod(base, exponent, divisor):
    """
    The reduction steps in the cases where the exponent e is greater than 1 are based on the fact that,
    for any integers x, y, and m, we can find the remainder of x times y modulo m by computing separately the remainders of x modulo m and y modulo m,
    multiplying these, and then taking the remainder of the result modulo m.
    (x * y) % m == ((x % m) * (y % m)) % m
    x ** 2n % m == (((x ** n) ** 2) % m == ((x ** n) * (x ** n)) % m == ((x ** n % m) * (x ** n % m)) % m
    For instance, in the case where e is even, we compute the remainder of b to the e/2th modulo m, square this, and take the remainder modulo m.
    This technique is useful because it means we can perform our computation without ever having to deal with numbers much larger than m.
    :param base:
    :param exponent:
    :param divisor:
    :return:
    """
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return (expmod(base, exponent // 2, divisor) ** 2) % divisor
    return (base * expmod(base, exponent - 1, divisor)) % divisor


def check_if_prime_fermat(integer):
    if integer in [0, 1, 4]:
        return False
    base = 1 + randint(0, integer - 2)
    return expmod(base, integer, integer) == base


def fast_prime(integer, times):
    if times == 0:
        return True
    elif check_if_prime_fermat(integer):
        return fast_prime(integer, times - 1)
    else:
        return False

