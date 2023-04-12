# Get the square of a number without ** or * or pow()
# https://www.codewars.com/kata/get-the-square-of-a-number-without-star-star-or-star-or-pow/train/python


def square0(n):
    q = 0
    for i in range(n):
        q += n
    return q


def square(n):
    return sum([n for i in range(n)])


def main():
    print(square(5))


if __name__ == '__main__':
    main()
