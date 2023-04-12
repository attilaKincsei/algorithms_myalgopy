##### Counting characters and %-age in a text ########

# N_PTB3_Vars&Scope.txt


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

chars_percent_dict = {}
for char in "abcdefghijklmnopqrstuvwxyz":  # Finding the percentage
    perc = 100 * count_char(text, char) / len(text)
    chars_percent_dict[char] = round(perc, 2)
    print("{0} - {1}%".format(char, round(perc, 2)))

chars_percent_list = []
for k, v in chars_percent_dict.items():
    chars_percent_list.append((k, v))

chars_percent_list.sort()  # sorting tuple pairs based on their first value

chars_percent_list2 = []
for k, v in chars_percent_dict.items():
    chars_percent_list2.append([k, v])

chars_percent_list2.sort()  # sorting sublists based on their first value


print(chars_percent_list)
print(chars_percent_list2)
# N_PTB3_Vars&Scope.txt

