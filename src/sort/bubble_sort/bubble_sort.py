# Sorting problem
# In computer science there is a recurring problem
# which is how to sort a list of numbers.
# In this assignment you get a flowchart of a possible solution
# and based on that you need to write the equivalent python script.
# This is a simple sorting algorithm
# that repeatedly steps through the list to be sorted,
# compares each pair of adjacent items and swaps them if they are in the wrong order.
#
# Implement the algorithm described by the flowchart in Python!
# Improve your solution:
# 1. Structure your code: separate some logic into functions.
# 2. Modify your program so that it asks the user to give the list of numbers.


def bubble_sort_ascending_while(list_to_sort):
    length = len(list_to_sort)

    iterations = 0

    while iterations < length - 1:

        j = 0

        while j < length - 1:

            if list_to_sort[j] > list_to_sort[j + 1]:

                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]

            j += 1

        iterations += 1

    return list_to_sort


def bubble_sort_ascending_for(list_to_sort):

    deep_copy = list_to_sort[:]

    list_length = len(deep_copy)

    iteration = list_length

    while(iteration > 1):
        iteration -= 1

        for j in range(list_length - 1):

            current = deep_copy[j]
            next = deep_copy[j + 1]

            if current > next:
                deep_copy[j], deep_copy[j + 1] = next, current

        list_length -= 1

    return deep_copy


def main():
    numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
    print(numbers)
    sorted_numbers = bubble_sort_ascending_for(numbers)
    print(sorted_numbers)

if __name__ == '__main__':
    main()