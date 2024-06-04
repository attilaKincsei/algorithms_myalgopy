from datetime import datetime


def count_words_single(file_path):
    with open(file_path) as file:
        file_content = file.read()
    row_list = file_content.split("\n")
    occurrence_single = dict()
    occurrence_duplicate = dict()
    for row in row_list:
        row_formatted = row.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '').replace('"', '').replace('(', '').replace(')', '').replace('`', '').replace('\'', '')
        if row_formatted not in [''] and 'page' not in row_formatted:
            word_list = map(lambda x: x.strip(), row_formatted.split(' '))
            for word in word_list:
                if occurrence_duplicate.get(word):
                    pass
                elif occurrence_single.get(word):
                    occurrence_duplicate[word] = occurrence_single.pop(word)
                else:
                    occurrence_single[word] = True
    return sorted(occurrence_single.keys())


if __name__ == '__main__':
    file_path_test = "/mnt/partData/DATABASE/00_datasets/ASOIAF/Ace_in_the_Hole_(Wild_Cards_06)_-_George_R.R._Martin.txt"
    start = datetime.now()
    result = count_words_single(file_path_test)
    end = datetime.now()
    print(result)
    print(len(result))  # 6202
    print(f"{end - start}")  # 88 ms (0:00:00.088194)
