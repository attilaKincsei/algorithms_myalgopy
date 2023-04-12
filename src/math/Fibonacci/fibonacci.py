import os

# Codecool fibonacce exercise:
# https://codecool.instructure.com/courses/74/pages/learning-to-program-with-python-part-1?module_item_id=15615
""" Variations 2
Use a dynamic number of spaces between the sequence id
(first, second, etc..) and the value,
to place the values into one column:"""


def get_input():
    """
    Getting user input for the length of Fibonacce sequence.
    """
    print('This is a Fibonacci sequence generator.')
    while True:
        try:
            userInput = input(
                "\nPlease enter a positive integer\nfor he number of Fibonacci numbers\nto be calculated and displayed: ")
            sequence_length = int(userInput)
        except ValueError as valerr:
            print('{0}. {1} is not a valid integer.'.format(valerr, userInput))
        else:
            break
    return sequence_length


def fibonacci():
    """Calculating Fibonacci numbers based on user input"""
    sequence_length = get_input()
    fibonacci_sequence = [0, 1]
    for i in range(sequence_length - 2):
        fibonacci_sequence.append(sum(fibonacci_sequence[-2:]))
    return fibonacci_sequence


def print_fibonacci():
    fibonacci_sequence = fibonacci()
    RIGHT_PADING = len(list(str(fibonacci_sequence[-1:])))
    os.system('clear')
    titles = ['Index', 'Fibonacci']
    print('{1[0]:<}{1[1]:>{0}}'.format(RIGHT_PADING, titles))
    for i in range(len(fibonacci_sequence)):
        print('{2:_<{0}}{3:_>{1}}'.format(
            len(titles[0]), RIGHT_PADING, (i + 1), fibonacci_sequence[i]))
    return fibonacci_sequence

# elem in zip(fibonacci_indices, fibonacci_sequence)
##################################################


def simple_fibonacci(sig, n):
    [sig.append(sum(sig[-2:])) for ctr in range(len(sig), n)]
    return sig[:n]


def main():
    test_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
                2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
    fib_seq = simple_fibonacci([1, 1], 10)
    print(fib_seq)
    sig = [1, 1]
    print(sum(sig[-2:]))


if __name__ == '__main__':
    main()
