from main.util.random_generator import generate_random_int_list
from main.util.decorators import measure_runtime


def no_arg_get_minimum():
    input_list = generate_random_int_list(100000, 1000000)
    minnn = input_list[0]
    for item in input_list:
        if item < minnn:
            minnn = item
    return minnn, input_list


def get_minimum(input_list):
    minimum = input_list[0]
    for item in input_list:
        if item < minimum:
            minimum = item
    return minimum


@measure_runtime
def get_minimum_with_runtime(input_list):
    minimum = input_list[0]
    for item in input_list:
        if item < minimum:
            minimum = item
    return minimum


def main():
    test_list = generate_random_int_list(100000, 1000000)

    rt1, minim1 = get_minimum_with_runtime(test_list)
    print(rt1)
    print(minim1)

    get_minimum_w_rt = measure_runtime(get_minimum)
    rt, minim = get_minimum_w_rt(test_list)
    print(rt)
    print(minim)


if __name__ == '__main__':
    main()
