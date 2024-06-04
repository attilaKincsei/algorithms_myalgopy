
"""
Exercise 1.11.
A function f is defined by the rule that
f(n) = n if n<3 and
f(n) = f(n - 1) + 2f(n - 2) + 3f(n -3) if n> 3.
Write a procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative process.
Scheme solution: https://sicp-solutions.net/post/sicp-solution-exercise-1-11/
Converted with: https://www.codeconvert.ai/free-converter
"""


def f_loop(n, n_1, n_2, n_3, nth):
    if n == nth:
        return n_1
    return f_loop(n, n_1 + 2 * n_2 + 3 * n_3, n_1, n_2, nth + 1)


def f_iterative(n):
    return n if n < 3 else f_loop(n, 2, 1, 0, 2)


def pascal(row, col):
    """
    Exercise 1.12.
    The following pattern of numbers is called Pascal's triangle.
    The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers above it.
    Write a procedure that computes elements of Pascal's triangle by means of a recursive process.
    """
    if row == 1:
        return 1
    elif col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col - 1) + pascal(row - 1, col)


def display_pascal_row(n):
    def column_iter(i):
        print(pascal(n, i), end="  ")
        if i == n:
            print()
        else:
            column_iter(i + 1)
    column_iter(1)


def display_pascal(n):
    def display_pascal_iter(i):
        display_pascal_row(i)
        if i == n:
            print()
        else:
            display_pascal_iter(i + 1)
    display_pascal_iter(1)


def _fast_expt_iter(accumulator, base, exponent):
    """
    Exercise 1.16
    Design a procedure that evolves an iterative exponentiation process
    that uses successive squaring and uses a logarithmic number of steps, as does .rec.expFast
    Hint:
    - Using the observation that (bn/2)2 = (b2)n/2, keep, along with the exponent n and the base b, an additional state variable a,
    and define the state transformation in such a way that the product a * b to the nth is unchanged from state to state.
    - At the beginning of the process a is taken to be 1, and the answer is given by the value of a at the end of the process.
    - In general, the technique of defining an invariant quantity that remains unchanged from state to state
    is a powerful way to think about the design of iterative algorithms.
    """
    if exponent == 0:
        return accumulator
    elif exponent % 2 == 0:
        return _fast_expt_iter(accumulator, base * base, exponent // 2)
    else:
        return _fast_expt_iter(accumulator * base, base, exponent - 1)


def fast_expt_iter(base, exponent):
    return _fast_expt_iter(1, base, exponent)


"""
Exercise 1.19.
There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps.
Let transformation T be: a + b -> a and a -> b.
Observe that applying T over and over again n times, starting with 1 and 0, produces the pair Fib(n + 1) and Fib(n).
In other words, the Fibonacci numbers are produced by applying Tn, the nth power of the transformation T,
starting with the pair (1,0).
Now consider T to be the special case of p = 0 and q = 1 in a family of transformations Tpq, where Tpq
transforms the pair (a,b) according to
bq + aq + ap -> a and
bp + aq -> b
Show that if we apply such a transformation Tpq twice,
the effect is the same as using a single transformation Tp'q' of the same form, and compute p' and q' in terms of p and q.
This gives us an explicit way to square these transformations, and thus we can compute Tn using successive squaring,
as in the fast-expt procedure.
Put this all together to complete the following procedure, which runs in a logarithmic number of steps:
(define (fib n)
  (fib-iter 1 0 0 1 n))

(define (fib-iter a b p q count)
  (cond ((= count 0)
         b)
        ((even? count)
         (fib-iter a
                   b
                   (+ (* p p) (* q q))    ;compute p'
                   (+ (* 2 q p) (* q q))  ;compute q'
                   (/ count 2)))
        (else
         (fib-iter (+ (* b q)
                      (* a q)
                      (* a p))
                   (+ (* b p)
                      (* a q))
                   p
                   q
                   (- count 1)))))
"""


def fib_sicp(n):
    return fib_iter_sicp(1, 0, 0, 1, n)


def fib_iter_sicp(a, b, p, q, count):
    if count == 0:
        return b
    elif count % 2 == 0:
        return fib_iter_sicp(a, b, p * p + q * q, 2 * q * p + q * q, count / 2)
    else:
        return fib_iter_sicp(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)


if __name__ == '__main__':
    print(fast_expt_iter(2, 1))
