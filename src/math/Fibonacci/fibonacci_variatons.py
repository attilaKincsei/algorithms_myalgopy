
############# Playing around with Fibonacci sequences ###############


def fibonacci(n):
    current, nexxt = 0, 1
    for i in range(n):
        current, nexxt = nexxt, current + nexxt
    return current


# printing all elements
def fibonacci_print(n):
    current, nexxt = 0, 1
    for i in range(n):
        current, nexxt = nexxt, current + nexxt
        print(current)

print(fibonacci_print(10))

# saving all elements of fib seq in a list
def fibonacci_list(n):
    current, nexxt = 0, 1
    fib_seq_list = [0]
    for i in range(n):
        current, nexxt = nexxt, current + nexxt
        fib_seq_list.append(current)
    return fib_seq_list


# making a generator function out of the fibonacci sequence:
# makes all lists from 1 element to the nth element
def fibonacci_generator(n):
    current, nexxt = 0, 1
    fib_seq_list = [0]
    for i in range(n):
        current, nexxt = nexxt, current + nexxt
        fib_seq_list.append(current)
        yield fib_seq_list


print(fibonacci_generator(10))


# fibonacce sequence with a generator function (no list)
def fibonacci_element_generator(n):
    current, nexxt = 0, 1
    for i in range(n):
        current, nexxt = nexxt, current + nexxt
        yield current


for elem in fibonacci_generator(20):
    print(elem)


### more fibonacci number generators:

# solution 1
fibSeq = [0, 1]
for i in range(28):
    last = fibSeq[-1] + fibSeq[-2]
    fibSeq.append(last)

print(fibSeq)


# solution 2
fibSeq2 = [0, 1]
for i in range(28):
    last = fibSeq2[-1] + fibSeq2[-2]
    fibSeq2.append(last)
    print(last)



# solution 3

print('This is a Fibonacci sequence generator.')
userInput = input \
    ("\nPlease enter a positive integer\nfor he number of Fibonacci numbers\nto be calculated and displayed: ")
FIB_SEQ_LEN = int(userInput) - 2
print('Fibonacci sequence:')
lastB1 = 0
print('{:<}: {:>}'.format(1, lastB1))
last = 1
print('{:<}: {:>}'.format(2, last))
for i in range(FIB_SEQ_LEN):
    temp = last
    last = lastB1 + last
    lastB1 = temp
    RIGHT_PAD = len(list(str(last)))
    print('{:<}: {:>{}}'.format(i + 3, last, (RIGHT_PAD + 2)))


## Memoized recursive Fibonacci sequences:
# http://ujihisa.blogspot.hu/2010/11/memoized-recursive-fibonacci-in-python.html

# A slow literal implementation of fibonacci function in Python is like the below:

def fib(n):
    return n if n < 2 else fib( n -2) + fib( n -1)


# This is slow but you can make it faster with memoize technique, reducing the order.

__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib( n -2) + fib( n -1)
        return __fib_cache[n]


# This is fast, but obviously dirty.
# Fortunately Python has decorator feature that gives you much better way of writing.

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
    return n if n < 2 else fib( n -2) + fib( n -1)

#####x## Tribonacci  ################
def tribonacci(signature, n):
    if n < 4:
        fibonacci_sequence = signature[0:n]
    else:
        fibonacci_sequence = signature[:]
        lastB2 = signature[0]
        lastB1 = signature[1]
        last = signature[2]
        for i in range((n - len(signature))):
            temp = last
            last = lastB2 + lastB1 + last
            fibonacci_sequence.append(last)
            lastB2 = lastB1
            lastB1 = temp
    return fibonacci_sequence


signature1 = [1, 1, 1]
print(tribonacci(signature1, 10))


# best solution 1:
def tribonacci_other1(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


# best solution 2:
def tribonacci_other2(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


# my solution after refactoring:
def tribonacci2(signature, n):
    tribonacci_sequence = signature[:]
    if n <= 3:
        tribonacci_sequence = signature[:n]
    else:
        for i in range(n - 3):
            tribonacci_sequence.append(sum(tribonacci_sequence[-3:]))
    return tribonacci_sequence
