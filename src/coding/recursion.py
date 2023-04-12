
"""
#####   Recursion   ####
!!!!!!! Always define a base case for recursive functions first to avoid stackoverflow and program crash

"""

# prime number generator
def is_prime(num):
    return None


def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
            num += 1



### Factorial calculation with recursion:
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

# Indirect recursion: two functions calling each other:
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


### Fibonacci with recursion:
def fibonacci0(n):  # dangerous, not failsafe, will throw a RuntimeError after 6765
    # calls to self
    print(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci0(n - 1) + fibonacci0(n - 2)


counter = 0
def fib_tail_recursion(length, signature):
    global counter
    counter = counter + 1
    if len(signature) == length:
        return signature
    print(counter)
    print(signature)
    signature.append(signature[-2] + signature[-1])
    return fib_tail_recursion(length, signature)

def practice():
    my_list = [1, 2, 3, 4, 5]
    return my_list


def fib_recursion(length, signature):
    global counter
    counter = counter + 1
    if len(signature) == length:
        return signature
    print("Before")
    print(counter)
    print(signature)
    signature.append(signature[-2] + signature[-1])
    signature = fib_recursion(length, signature)
    print("After")
    print(counter)
    print(signature)
    return signature[0:-1]


if __name__ == '__main__':
    fib_recursion(10, [1, 1])
    # print(fib_tail_recursion(10, [1, 1]))
    # print(len(practice()))

