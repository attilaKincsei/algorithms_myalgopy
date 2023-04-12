from time import time
from timeit import timeit
from main.algorithms.coding.minmaxavg.minmaxavg import get_minimum, no_arg_get_minimum, get_minimum_with_runtime
from main.util.random_generator import generate_random_int_list, generate_random_int_list_with_runtime
from main.util.decorators import remove_parameters_and_create_closure, measure_runtime

# minmaxavg
# Calculate minimum, maximum and average from numbers in a list.
# https://codecool.instructure.com/courses/74/assignments/2494?module_item_id=15622
# PLEASE DO NOT USE BUILT-IN PYTHON FUNCTIONS TO CALCULATE MIN, MAX, AND AVG!
# Those forbidden functions are: min(), max(), sum(), sort(), sorted() etc. 


"""
1. Let's assume we've got a list:
numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
2. Please create three flowcharts for calculating
  the maximum,
  minimum and
  average number
  for above list (you can use draw.io).
3. After this, please create a python script
that will implement above flowcharts.

"""


def setup_test_get_min(tester, max_power_of_ten):
    maximum = 1000000
    print("Range of possible integers to choose from: -{0} - {0}".format(maximum))
    print("----------------------------------------------------")
    input_power = min(8, max_power_of_ten + 1)
    for power in range(1, input_power):
        test_list = generate_random_int_list(10 ** power, maximum)
        print("Number of elements in list: 1" + "0" * power)
        tester(test_list)


def test_get_min(test_input):
    is_passed = min(test_input) == get_minimum(test_input)
    result = "OK!" if is_passed else "Test Failed"
    print(result)


def test_no_arg_get_min():
    actual, test_input = no_arg_get_minimum()
    expected = min(test_input)
    result = "OK!" if expected == actual else "Test Failed"
    print(result)


def test_get_min_with_runtime(test_input):
    expected = min(test_input)
    elapsed, actual = get_minimum_with_runtime(test_input)
    result = "OK!" if expected == actual else "Test Failed"
    print(result)
    print("Runtime in milliseconds: {0}".format(elapsed))


def test_generate_random_list_with_runtime(input_power):
    for power in range(min(8, input_power + 1)):
        elapsed, actual = generate_random_int_list_with_runtime(10 ** power, 10000)
        print(actual[0:100], end="\n")
        print("Runtime in milliseconds: {0}".format(elapsed))


"""
4. (optional) Now, the list looks a bit different:
numbers2 = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]
Update your python script to maintain
  it's previous functionality - please,
      ignore non-numbers and
      search for numbers inside nested list!
"""

# Data for average:
numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
numbers2 = [0.2, -5, 23, 0, "dupa", -9, 12, 99, [[10], 0.3, 2, 44, None, "rrr"], None, 105, -43]


def main():
    test_list = generate_random_int_list(100000, 10000)
    get_minimum_w_rt = measure_runtime(get_minimum)
    rt, minim = get_minimum_w_rt(test_list)
    print(rt)
    print(minim)
    # test_generate_random_list_with_runtime(8)

    # test_get_min_with_runtime(test_list)
    # setup_test_get_min(test_get_min_with_runtime, 7)

    # get_minimum2 = remove_parameters_and_create_closure(get_minimum, test_list)
    # print(timeit(stmt=get_minimum2, number=10))

    # test_no_arg_get_min()


if __name__ == '__main__':
    main()
