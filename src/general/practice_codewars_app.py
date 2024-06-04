import re
from functools import partial
from itertools import permutations


def digital_root(n):
    if 10 > n:
        return n
    return digital_root(sum(map(int, list(str(n)))))


def greet_one(name):
    return "Hello, " + ("my love" if name == "Johnny" else name) + "!"


def greet(name):
    name = "mark_bowman"
    return "Hello, {addressee}!".format(addressee="my love" if name == "Johnny" else name)


def find_needle(haystack):
    haystack = ['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']
    sentinel_value = "needle"
    for i, hay in enumerate(haystack):
        if hay == sentinel_value:
            break
    else:
        return "{sv} not found".format(sv=sentinel_value)
    return "found the {sv} at position {index}".format(sv=sentinel_value, index=i)


def highest_rank_mine(arr):
    arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]
    rank_dict = dict()
    for integer in arr:
        rank_dict[integer] = 1 + rank_dict.get(integer, 0)
    return sorted(sorted(list(map(list, rank_dict.items())), key=lambda a: a[0], reverse=True), key=lambda a: a[1], reverse=True)[0][0]


def highest_rank(arr):
    """
    Sorts the array in reverse order before finding the maximum in order to get the largest element in case of multiple maximum values
    """
    return max(sorted(arr, reverse=True), key=arr.count)


def alphanumeric_mine(password):
    return False if "_" in password else bool(re.fullmatch(r"(\w+)", password))


def alphanumeric(password):
    return password.isalnum()


def rolling_sum(array, length):
    if len(array) == 0:
        return [0]
    if length == 0:
        return [0] * len(array)

    rolling_sum_array = []
    for i in range(len(array)):
        upper_endpoint = i + 1
        rolling_sum_array.append(sum(array[max([0, upper_endpoint - length]):upper_endpoint]))

    return rolling_sum_array


def max_subarray(arr):
    if arr == [] or sum(arr) + sum(map(abs, arr)) == 0:
        return 0
    if sum(arr) == sum(map(abs, arr)):
        return sum(arr)

    rolling_sum_partial = partial(rolling_sum, arr)
    sub_array_length_range = range(1, len(arr) - 1)
    rolling_sum_matrix = list(map(rolling_sum_partial, sub_array_length_range))

    sub_array_max_list = list(map(max, rolling_sum_matrix))
    sub_array_max = max(sub_array_max_list)
    sub_array_length = list(sub_array_length_range)[sub_array_max_list.index(sub_array_max)]
    sub_array_upper_endpoint = max(rolling_sum_matrix, key=max).index(sub_array_max) + 1
    sub_array_lower_endpoint = sub_array_upper_endpoint - sub_array_length
    return arr[sub_array_lower_endpoint:sub_array_upper_endpoint]


def max_sequence(arr):
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6
    if len(arr) == 0 or sum(arr) + sum(map(abs, arr)) == 0:
        return 0
    if sum(arr) == sum(map(abs, arr)):
        return sum(arr)

    rolling_sum_partial = partial(rolling_sum, arr)
    rolling_sum_matrix = list(map(rolling_sum_partial, range(0, len(arr) + 1)))
    return max(list(map(max, rolling_sum_matrix)))


def sorter(textbooks):
    textbooks = ['Algebra', 'History', 'Geometry', 'English']
    return sorted(textbooks)


def digitize(n):
    n = 35231
    return list(map(int, str(n)[::-1]))


def valid_parentheses(string):
    string = "("
    string = "((((((((((((((((((()"
    string = "(((((((()())))))))"
    string = ")()"
    string = "())("
    string = "())(()"
    string = "()hi()"
    parenthesis_open = "("
    parenthesis_close = ")"
    parenthesis_value_map = {parenthesis_open: 1, parenthesis_close: -1}

    valid_parentheses_total = 0
    irrelevant_character_value = 0
    counter = valid_parentheses_total

    for character in string:
        counter += parenthesis_value_map.get(character, irrelevant_character_value)
        if counter < valid_parentheses_total:
            return False
    else:
        return counter == valid_parentheses_total


def validate_battlefield(battle_field):
    battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    fleet0 = {"battleships": [[1, 1, 1, 1]],
              "cruisers": [[1, 1, 1], [1, 1, 1]],
              "destroyers": [[1, 1], [1, 1], [1, 1]],
              "submarines": [[1], [1], [1], [1]]}

    fleet = {"battleships": 4,
             "cruisers": 6,
             "destroyers": 6,
             "submarines": 4}

    return sum(list(fleet0.values()))

    if sum(list(map(sum, battle_field))) != sum(list(fleet.values())):
        return False

    for i, row in enumerate(battle_field):
        for j, field in enumerate(row):
            if field == 1:
                neighbor_index_col_prev = i - 1
                neighbor_index_col_next = i + 1
                neighbor_index_row_prev = j - 1
                neighbor_index_row_next = j + 1

                forbidden_field1 = False if neighbor_index_col_prev < 0 or neighbor_index_row_prev < 0 else 1 == battle_field[neighbor_index_col_prev:neighbor_index_row_prev]
                forbidden_field2 = False if neighbor_index_col_prev < 0 or neighbor_index_row_next < 0 else 1 == battle_field[neighbor_index_col_prev:neighbor_index_row_next]
                forbidden_field3 = False if neighbor_index_col_next < 0 or neighbor_index_row_prev < 0 else 1 == battle_field[neighbor_index_col_next:neighbor_index_row_prev]
                forbidden_field4 = False if neighbor_index_col_next < 0 or neighbor_index_row_next < 0 else 1 == battle_field[neighbor_index_col_next:neighbor_index_row_next]

                if forbidden_field1 or forbidden_field2 or forbidden_field3 or forbidden_field4:
                    return False
    return True


def next_smaller_inefficient(n):
    n = 937
    n = 907
    n = 10
    n = 2071
    n = 1702
    n = 315
    n = 10234
    n = 10
    n = 135

    no_smaller_number = -1
    n_string = str(n)
    if len(n_string) == 1:
        return no_smaller_number
    permutations_sorted = sorted(list(map("".join, list(map(list, permutations(n_string))))))
    permutations_sorted_index = permutations_sorted.index(n_string)
    if permutations_sorted_index == 0:
        return no_smaller_number
    next_smaller_string = permutations_sorted[permutations_sorted_index - 1]
    return no_smaller_number if '0' == next_smaller_string[0] else int(next_smaller_string)


def next_smaller(n):

    n = 937
    n = 907
    n = 10
    n = 2071
    n = 1702
    n = 315  # 153 (not 135)

    no_smaller_number = -1
    digit_tuple = tuple(str(n))
    if len(digit_tuple) == 1:
        return no_smaller_number
    next_smaller_num = no_smaller_number
    for i in range(len(digit_tuple) - 1, -1, -1):
        print(f"i: {i}")
        # digit_list = list(digit_tuple)
        for j in range(len(digit_tuple) - 1 - (len(digit_tuple) - i), -1, -1):
            print(f"j: {j}")
            digit_list = list(digit_tuple)
            if digit_tuple[i] < digit_tuple[j]:
                digit_list.insert(j, digit_list.pop(i))
                if digit_list[0] == '0':
                    pass
                else:
                    smaller_num = int("".join(digit_list))
                    print(f"smaller_num: {smaller_num}")
                    if next_smaller_num < smaller_num < n:
                        next_smaller_num = smaller_num
                    print(f"next_smaller_num: {next_smaller_num}")
    return next_smaller_num


def validate_parentheses(string):
    parenthesis_open = "("
    parenthesis_close = ")"
    parenthesis_value_map = {parenthesis_open: 1, parenthesis_close: -1}

    valid_parentheses_total = 0
    irrelevant_character_value = 0
    counter = valid_parentheses_total

    for character in string:
        counter += parenthesis_value_map.get(character, irrelevant_character_value)
        if counter < valid_parentheses_total:
            return False
    else:
        return counter == valid_parentheses_total


def balanced_parens(n):

    n = 0
    n = 1
    n = 2

    if n == 0:
        return [""]
    parenthesis_open = "("
    parenthesis_close = ")"

    parentheses_base = (parenthesis_open + parenthesis_close) * n
    parenthesis_list = [parentheses_base]
    for i in range(1, len(parentheses_base) - 1):
        parentheses_base_list = list(parentheses_base)
        parentheses_base_list[i + 1], parentheses_base_list[i] = parentheses_base_list[i], parentheses_base_list[i + 1]
        parenthesis_list.append("".join(parentheses_base_list))
    return parenthesis_list


if __name__ == '__main__':
    print(balanced_parens(""))
