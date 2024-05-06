from time import time


def remove_parameters_and_create_closure(func, *args, **kwargs):
    """
    decorator to remove arguments from a function
    :param func:
    :param args:
    :param kwargs:
    :return:
    """

    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def measure_runtime(func):
    """
    decorator to add extra behaviour to func, while retaining its parameters
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        start_in_millis = int(time() * 1000)
        result = func(*args, **kwargs)
        end_in_millis = int(time() * 1000)
        return end_in_millis - start_in_millis, result

    return wrapper
