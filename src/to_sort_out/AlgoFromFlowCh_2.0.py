numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]

print(numbers)

# function for ascending order
def sort_fun(x):
    N = len(x)
    iterations = 1
    while iterations < N:
        j = 0
        while j <= N - 2:
            if x[j] > x[j + 1]:
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
                j = j + 1
            else:
                j = j + 1
        iterations = iterations + 1
    return(x)

print(sort_fun(numbers))

# function for descending order
def sort_fun2(x):
    N = len(x)
    iterations = 1
    while iterations < N:
        j = 0
        while j <= N - 2:
            if x[j] < x[j + 1]:
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
                j = j + 1
            else:
                j = j + 1
        iterations = iterations + 1
    return(x)

print(sort_fun2(numbers))

# parameter for choosing ascending or descending:

"""Primitive sorter function.
x = list object
order = "d" descending order (default: [blank] ascending)
"""

def sorter_fun(x, order = "a"):
    N = len(x)
    iterations = 1
    if order == "d":  
        while iterations < N:
            j = 0
            while j <= N - 2:
                if x[j] < x[j + 1]:
                    temp = x[j + 1]
                    x[j + 1] = x[j]
                    x[j] = temp
                    j = j + 1
                else:
                    j = j + 1
            iterations = iterations + 1
        return(x)
    else:
        while iterations < N:
            j = 0
            while j <= N - 2:
                if x[j] > x[j + 1]:
                    temp = x[j + 1]
                    x[j + 1] = x[j]
                    x[j] = temp
                    j = j + 1
                else:
                    j = j + 1
            iterations = iterations + 1
        return(x)

numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]

print(numbers)
print(sorter_fun(numbers, "d"))
