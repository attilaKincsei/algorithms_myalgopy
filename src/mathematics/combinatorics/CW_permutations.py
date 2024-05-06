def permutations(string):

    string_list = list(string)
    permutations_list = [string_list[:]]

    for i in range(len(string_list)):
        for j in range((i + 1), len(string_list)):
            temporary_string_list = string_list[:]
            temporary_string_list[i], temporary_string_list[j] = string_list[j], string_list[i]
            permutations_list.append(temporary_string_list)

    for i in range(len(string_list)):
        for j in range((i + 1), len(string_list)):
            temporary_string_list2 = string_list
            temporary_string_list2[i], temporary_string_list2[j] = string_list[j], string_list[i]
            permutations_list.append(temporary_string_list2)

    for i in range(len(permutations_list)):
        permutations_list[i] = ''.join(permutations_list[i])

    return sorted(set(permutations_list))


def main():
    print(permutations('a')) # ['a']
    print(permutations('ab'))  # ['ab', 'ba']
    print(permutations('aabb'))  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']


if __name__ == '__main__':
    main()