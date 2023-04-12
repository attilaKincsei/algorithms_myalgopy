from math import factorial

# for j in range((i + 1), len(permutation_list)):

test_string = "jhglkjhriouthfljbnkjfgh"
test_string2 = "mississippi"
test_string3 = 'aabb'

def number_of_permutations_of_multisets(string):
    """
    Permutations of multisets: n! / m1!*m2!*...*mk!
    :param string: a string
    :return: the number of multiset permutations
    """
    string_list = list(string)
    n_factorial = factorial(len(string_list))
    letter_counter = {}
    for letter in string_list:
        letter_counter[letter] = 0
    for letter in string_list:
        letter_counter[letter] += 1
    for k, v in letter_counter.items():
        n_factorial /= factorial(v)
    return n_factorial

def permutations(string):
    string_list = list(string)
    permutation_list = [string_list[:]]
    for i in range(len(string_list)):
        for j in range(len(string_list)):
            temporary_string_list = string_list[:]
            temporary_string_list[i], temporary_string_list[j] = string_list[j], string_list[i]
            permutation_list.append(temporary_string_list)
    print(permutation_list)
    for i in range(len(permutation_list)):
        permutation_list[i] = ''.join(permutation_list[i])
    permutation_set = set(permutation_list)
    return_permutation_list = list(permutation_set)
    return return_permutation_list


print(permutations(test_string3))