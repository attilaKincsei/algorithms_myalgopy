"""
Always define a base case for recursive function to avoid
stackoverflow and program crash
"""


## generating the nth element of a Fibonacci sequence
# with a recursive function:


## Any recursive function can be re-written in an iterative way which avoids
# recursion
# same fibonacci function written in an iterative way:


### Fibonacci with recursion:
def fibonacci0(n):  # dangerous, not failsafe, will throw a RuntimeError after 6765
    # calls to self
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci0(n - 1) + fibonacci0(n - 2)


def fib_tail_recursion(length, signature):
    if len(signature) == length:
        return signature
    signature.append(signature[-2] + signature[-1])
    return fib_tail_recursion(length, signature)


# Memoized recursive Fibonacci sequences:
# http://ujihisa.blogspot.hu/2010/11/memoized-recursive-fibonacci-in-python.html

# A slow literal implementation of fibonacci function in Python is like the
# below:

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


# This is slow but you can make it faster with memoize technique, reducing
# the order.

__fib_cache = {}


def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n - 2) + fib(n - 1)
        return __fib_cache[n]


# This is fast, but obviously dirty.

### _Recursion_, _memoization_ and _decorators_ illustrated with fibonacci
# sequences:
# Fortunately Python has decorator feature that gives you much better way of
# writing.

def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorated_function


@memoize
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def main():
    print(fibonacci0(10))


if __name__ == '__main__':
    main()
