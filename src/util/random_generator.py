from random import randint, choice
from util.decorators import measure_runtime


def generate_random_int_list(n, value_range):
    return [randint(0, value_range) * choice([-1, 1]) for i in range(n)]


@measure_runtime
def generate_random_int_list_with_runtime(n, value_range):
    return [randint(0, value_range) * choice([-1, 1]) for i in range(n)]

