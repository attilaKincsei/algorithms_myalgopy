### Invert values:
-elem = elem * -1

### Parse nice int from char problem:
'stringg'[0] == list('stringg')[0] == 's'

### Is this a triangle?

# pure genius: just return if condition if bool vaue is in question:
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        booll = True
    else:
        booll = False
    return booll


### Counting in the Amazon

# ' '.join method returns iterable elements joined by value between ''.join()
def count_arara(n):
    return ' '.join((n // 2) * ['adak'] + (n % 2) * ['anane'])


def count_arara(n):
    arara = (n // 2) * 'adak ' + (n % 2) * 'anane'
    if arara[-1:] == ' ':
        arara_rv = arara[:-1]
    else:
        arara_rv = arara
    return arara_rv


### Functional addition:
# if you want to use the parameter of a function in a nested function,
# just give it as a keywork argument: n=n
def add(n):
    def add_number(x, n=n):
        x + n
        return x + n
    return add_number


# how to write tests in codewars, if i have time for it:
# in python:
# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/development.html
# https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137

# in codewars:
# https://github.com/Codewars/codewars.com/wiki/Codewars-Python-Test-Framework
# https://www.codewars.com/docs/python-test-reference-1
# https://www.codewars.com/docs/kata-test-framework



### Do you know how to make Query String?
# https://www.codewars.com/kata/do-you-know-how-to-make-query-string/train/python
# query string: https://en.wikipedia.org/wiki/Query_string
# - dictionaries can have multiple values per keys:
# {'ad': [2, 3], ...}

# 

data = {'a': [1, 1.1, 1.2], 'b': [2, 2.1], 'c': 3, 'd': ['a', 'f', 'b', '0']}


def to_query_string(data):
    joined_kv = []
    for k, v in data.items():
        if isinstance(v, (list, tuple, set)):
            for elem in v:
                joined_kv.append([str(k), str(elem)])
        else:
            joined_kv.append([str(k), str(v)])
    sorted_kv = sorted(joined_kv, key=lambda x: x[0][0])
    sorted_joined_kv = []
    for pair in sorted_kv:
        sorted_joined_kv.append('='.join(pair))
    query_string = '&'.join(sorted_joined_kv)
    return query_string


print(to_query_string(data))


# best solution1:
def to_query_string(data):
    result = []
    for key, value in sorted(data.items()):  # you can sort a dictionary by its keys
        if not isinstance(value, (list, tuple, set)):
            value = [value]  # clever to transform non-sequence type to a single element list
        for val in value:
            result.append("{}={}".format(key, val))  # wow, you can use format instead of .join()!!
    return "&".join(result)


def to_query_string(data):
    return '&'.join('{}={}'.format(a, d) if type(d) != list
                    else '&'.join('{}={}'.format(a, e) for e in d)
                    for a, d in sorted(data.items()))



### (kyu 6) Number of measurements to spot the counterfeit coin

def how_many_measurements(n):
    weighings = 0
    while n > 1:
        weighings += 1
        if n % 3 == 2:
            n = (n + 1) // 3
        elif n % 3 == 1:
            n = (n + 2) // 3
        else:
            n //= 3
    return weighings


# best solution 1:
from mathematics import ceil, log


def how_many_measurements(n):
    return ceil(log(n, 3))


## bowling pins (kyu 6)

def bowling_pins(arr):
    bowling_pins_graphic = 'I I I I\n I I I \n  I I  \n   I   '
    bowling_pins_graphic_list = list(bowling_pins_graphic)
    bowling_pins_graphic_dictionary = {1: 27, 3: 20, 2: 18, 4: 9, 5: 11, 6: 13, 7: 0, 8: 2, 9: 4, 10: 6}
    for elem in arr:
        bowling_pins_graphic_list[bowling_pins_graphic_dictionary[elem]] = ' '
    bowling_pins_graphic = ''.join(bowling_pins_graphic_list)
    return bowling_pins_graphic


remove_list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_list1 = [2, 3, 4, 8, 9, 10]
remove_list2 = []
print(bowling_pins(remove_list2))


# best solutions:
def bowling_pins_best(arr):
    pins = "{7} {8} {9} {10}\n" + \
            " {4} {5} {6} \n" + \
            "  {2} {3}  \n" + \
            "   {1}   "
    return pins.format(*(" " if i in arr else "I" for i in range(11)))


# in full form, my refactoring:
def bowling_pins_best_refactored(arr):
    pins = "{7} {8} {9} {10}\n" + " {4} {5} {6} \n" + "  {2} {3}  \n" + "   {1}   "
    replacement_list = []
    for i in range(11):
        if i in arr:
            replacement_list.append(' ')
        else:
            replacement_list.append('I')
    return pins.format(*replacement_list)


## best solution 2
def bowling_pins(empty):
    raw = ['I ', 'I ', 'I ', 'I\n', ' I', ' I ', 'I \n', '  I ', 'I  \n', '   I   ']
    replace = ['  ', '  ', '  ', ' \n', '  ', '   ', '  \n', '    ', '   \n', '       ']
    order = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]

    return ''.join([replace[x] if order[x] in empty else raw[x] for x in range(10)])


### what i learnt from this exercise:
# - string formatting rules
# - make an empty field and fill them up according to arguments


## tribonacci

def tribonacci(signature, n):
    if n < 4:
        fibonacci_sequence = signature[0:n]
    else:
        fibonacci_sequence = signature[:]
        lastB2 = signature[0]
        lastB1 = signature[1]
        last = signature[2]
        for i in range((n - len(signature))):
            temp = last
            last = lastB2 + lastB1 + last
            fibonacci_sequence.append(last)
            lastB2 = lastB1
            lastB1 = temp
    return fibonacci_sequence


signature1 = [1, 1, 1]
print(tribonacci(signature1, 10))


# best solution 1:
def tribonacci_other1(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


# best solution 2:
def tribonacci_other2(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


# my solution after refactoring:
def tribonacci2(signature, n):
    tribonacci_sequence = signature[:]
    if n <= 3:
        tribonacci_sequence = signature[:n]
    else:
        for i in range(n - 3):
            tribonacci_sequence.append(sum(tribonacci_sequence[-3:]))
    return tribonacci_sequence


### bee hive

# sol1:
def how_many_bees1(hive):
    number_of_the_bees = 0
    if hive is None:
        number_of_the_bees = 0
    elif len(hive) == 0:
        number_of_the_bees = 0
    else:
        transposed_beehive = [[] for i in range(len(hive[0]))]
        for i in range(len(hive)):
            row_string = ''.join(hive[i])
            number_of_the_bees += row_string.count('bee')
            number_of_the_bees += row_string.count('eeb')
            for j in range(len(hive[i])):
                transposed_beehive[j].append(hive[i][j])
        for column in transposed_beehive:
            column_string = ''.join(column)
            number_of_the_bees += column_string.count('bee')
            number_of_the_bees += column_string.count('eeb')
    return number_of_the_bees

# sol2:
def how_many_bees(hive):
    number_of_the_bees = 0
    if hive is None:
        number_of_the_bees = 0
    elif len(hive) == 0:
        number_of_the_bees = 0
    else:
        transposed_beehive = [[] for i in range(len(hive[0]))]
        for i in range(len(hive)):
            row_string = ''.join(hive[i])
            number_of_the_bees += row_string.count('bee')
            number_of_the_bees += row_string.count('eeb')
            for j in range(len(hive[i])):
                transposed_beehive[j].append(hive[i][j])
        for column in transposed_beehive:
            column_string = ''.join(column)
            number_of_the_bees += column_string.count('bee')
            number_of_the_bees += column_string.count('eeb')
    return number_of_the_bees


# print(*(hive), sep='\n')
# print(*(transposed_beehive), sep='\n')

hive = ["bee.bee", "e.e.e.e", "eeb.eeb"]
hive2 = [list("bee.bee"), list("e.e.e.e"), list("eeb.eeb")]
print(how_many_bees(hive2))  # 8



######## Sum of Digits / Digital Root ##########

def digital_root(n):
    if n < 10:
        sum_of_digits = n
    else:
        number_of_digits = len(str(n))
        string_digits_list = list(str(n))
        while number_of_digits > 1:
            sum_of_digits = 0
            for elem in string_digits_list:
                sum_of_digits += int(elem)
            number_of_digits = len(str(sum_of_digits))
            string_digits_list = list(str(sum_of_digits))
    return sum_of_digits


# best solution1:
def digital_root1(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# best solution2:
def digital_root2(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n

## my solution after best solutions:
def digital_root(n):
    while n > 9:
        n = sum(map(int, list(str(n))))
    return n


### IP validation
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
def is_valid_IP(strng):
    IP_octet_list = strng.split('.')
    if len(IP_octet_list) != 4:
        return False
    for i, octet in enumerate(IP_octet_list):
        try:
            int(octet)
        except ValueError as valerr:
            print(valerr)
            return False
        else:
            is_octet_between_0_and_255 = (-1 < int(octet) < 256)
            is_length_between_1_and_3 = 0 < len(octet) < 4
            is_octet_starts_with_non_0 = octet == str(int(octet))
            if is_octet_between_0_and_255 and is_length_between_1_and_3 and is_octet_starts_with_non_0:
                is_valid_IP_true = True
            else:
                return False
    return is_valid_IP_true


def main():
    test_IP_string = '192.168.1.19'
    test_IP_string2 = '1.2.01.019'
    test_IP_string3 = '111.21.1.1119'
    test_IP_string4 = '11.1.1.019'
    test_IP_string5 = '1.192.1.19s'
    test_IP_string6 = '1,192.1.255'
    test_IP_string7 = '1.192.1.256'
    test_IP_string8 = '1.192.1.253.1'
    test_is_valid_IP = {
        test_IP_string: True, test_IP_string2: False, test_IP_string3:
        False, test_IP_string4: False, test_IP_string5: False, test_IP_string6: False,
        test_IP_string7: False, test_IP_string8: False
    }

    for test, boolean in test_is_valid_IP.items():
        if bool(is_valid_IP(test) == boolean):
            print("OK!")
        else:
            print("Failure!")


if __name__ == '__main__':
    main()


# best solutions:
def is_valid_IP(strng):
    lst = strng.split('.')
    passed = 0
    for sect in lst:
        if sect.isdigit():
            if sect[0] != '0':
                if 0 < int(sect) <= 255:
                    passed += 1
    return passed == 4


# with re module
import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))


## my solution after refactoring:
def is_valid_IP_refact(strng):
    IP_octet_list = strng.split('.')
    is_true_number = 0
    for octet in IP_octet_list:
        if octet.isdigit():
            if 0 < len(octet) < 4:
                if octet == str(int(octet)):
                    if 0 <= int(octet) < 256:
                        is_true_number += 1
    return is_true_number == 4
