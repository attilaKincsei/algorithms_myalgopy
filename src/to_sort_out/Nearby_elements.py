### Find and return the nearby elements from a two-dimensional int array  ##


def nearby_elements(integer_array, x, y, interval):
    if y < len(integer_array[x]):
        target_element = integer_array[x][y]
        left_endpoint = y - min(y, interval)
        right_endpoint = min((y + interval + 1), len(integer_array[x]))
        array_slice = integer_array[x][left_endpoint:right_endpoint]
        array_slice.remove(target_element)
        return array_slice


# test variables:
# nearby(0, 2, 2) would result: [2, 0, 1241, 12]
# nearby(1, 0, 1) would result: [3]
# nearby(1, 3, 5) would result: [1, 3, 5]

java_array = [
    [2, 0, 4, 1241, 12, 5, 11, 1110, -42, 424, 1, 12323 ],
    [1, 3, 5, 7 ],
    [321, 320, 32, 3, 41241, -11, -12, -13, -66, -688 ]
]

print(nearby_elements(java_array, 0, 2, 2))


