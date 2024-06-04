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


def simple_tribonacci(sig, n):
    [sig.append(sum(sig[-3:])) for ctr in range(len(sig), n)]
    return sig[:n]
