from string import punctuation
"""
https://www.codewars.com/kata/most-frequently-used-words-in-a-text/train/python
"""


def top_3_words(text):
    word_counter = {}
    split_by_spaces = text.split(" ")
    for elem in split_by_spaces:
        items = elem.strip(punctuation).strip()
        current_value = word_counter.setdefault(items, 0)
        word_counter[items] = current_value + 1

    if '' in word_counter.keys():
        del word_counter['']

    word_counter_list = list(word_counter.items())

    sorted_by_keys = sorted(word_counter_list, key=lambda x: x[0])
    sorted_by_values_and_keys = sorted(sorted_by_keys, key=lambda x: x[1], reverse=True)

    lower_sorted_list = [item[0].lower() for item in sorted_by_values_and_keys]
    return lower_sorted_list[:min(len(lower_sorted_list), 3)]


def assert_equals(actual, expected):
    has_passed = "OK!" if actual == expected else "FAIL"
    print(has_passed)


def main():
    print(punctuation.replace("'", " "))
    # result = top_3_words("q w w w w W e e e r r t z h g f / d dddd     \"'/.!?")
    # result2 = top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
    # print(result2)
    # print(result2[1] == result2[2])
    assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
    assert_equals(top_3_words("  , e   .. "), ["e"])
    assert_equals(top_3_words("  ...  "), [])
    assert_equals(top_3_words("  '  "), [])
    assert_equals(top_3_words("  '''  "), [])
    assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])


if __name__ == '__main__':
    main()
