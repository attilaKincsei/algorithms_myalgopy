
from functools import partial
import practice_class as pc


def test_diadic(arg1, arg2, arg3):
    return arg1 % arg2 * arg3


def test_diadic_curry(arg3):
    return test_diadic(5, 3, arg3)


def partial_practice():
    proj = partial(test_diadic, 10, 2)
    return proj(5)


def main():
    pr_class = pc.PracticeClass(5)
    result = pr_class.practice_method(10)
    return result


if __name__ == '__main__':
    int_var = ["15", "asfd"]
    print(type(int_var))
    print(type(pc))
    print(type(main))
    print(partial_practice())
    print(test_diadic_curry(101))
