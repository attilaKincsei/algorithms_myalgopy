
"""
#Assignment: MinMaxAvg
PLEASE DO NOT USE BUILT-IN PYTHON FUNCTIONS TO CALCULATE MIN, MAX, AND AVG!
 Those forbidden functions are: min(), max(), sum(), sort(), sorted() etc.

##The exercise
1. Let's assume we've got a list: numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

2. Please create three flowcharts for calculating the
 maximum, minimum and average number for above list (you can use draw.io ).

3. After this, please create a python script that will implement above flowcharts.

4. (optional) Now, the list looks a bit different:
 numbers = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]
  Update your python script to maintain its previous functionality
   - please ignore non-numbers and search for numbers inside nested list!

"""


def get_minimum(vector: list) -> int:
    minimum = vector[0]
    for item in vector:
        if item < minimum:
            minimum = item
    return minimum


def get_maximum(vector: list) -> int:
    maximum = vector[0]
    for item in vector:
        if item > maximum:
            maximum = item
    return maximum


def calculate_arithmetic_mean(vector: list) -> float:
    sum_of_vector = 0
    length = 0
    for element in vector:
        if type(element) not in [int, float, list]:
            continue
        if type(element) == list:
            for nested in element:
                sum_of_vector += nested
                length += 1
        else:
            sum_of_vector += element
            length += 1

    return sum_of_vector / length
