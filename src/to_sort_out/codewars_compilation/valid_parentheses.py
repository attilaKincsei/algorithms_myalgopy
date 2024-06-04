# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    if not string.strip():
        return True
    input_list = list(string)
    par_list = []
    for char in input_list:
        if char in "()":
            par_list.append(char)

    if len(par_list) % 2 != 0:
        return False

    if par_list.count("(") != par_list.count(")"):
        return False

    if par_list[0] == ")" or par_list[-1] == "(":
        return False

    return True


def main():
    test1 = "hi(hi)()"
    test2 = ""
    test3 = "())(()"
    print(valid_parentheses(test3))


if __name__ == '__main__':
    main()
