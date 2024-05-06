from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_datetime = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2_datetime = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    total_sec = abs(int(t1_datetime.timestamp() - t2_datetime.timestamp()))
    return str(total_sec)


def time_delta2(list_of_lists):
    results_list = []
    for pair in list_of_lists:
        t1_datetime = datetime.strptime(pair[0], "%a %d %b %Y %H:%M:%S %z")
        t2_datetime = datetime.strptime(pair[1], "%a %d %b %Y %H:%M:%S %z")
        total_sec = abs(int(t1_datetime.timestamp() - t2_datetime.timestamp()))
        results_list.append(str(total_sec))
    return results_list


def read_file(file_name):
    with open(file_name) as input_file:
        return input_file.read().split('\n')


def distribute_date_times(date_time_list):
    number_of_pairs = len(date_time_list)
    paired = []
    for i in range(0, number_of_pairs, 2):
        paired.append([date_time_list[i], date_time_list[i + 1]])
    return paired


def compare_results(expected, actual):
    is_same = True
    line = -1
    for i, expected_result in enumerate(expected):
        if expected_result != actual[i]:
            is_same = False
            line = i
            break
    return [is_same, line]


def main():
    date_time_list = read_file('time_delta_input01.txt')
    paired = distribute_date_times(date_time_list)
    result_list = time_delta2(paired)
    expected_list = read_file('time_delta_output01.txt')
    error = compare_results(expected_list, result_list)
    print(error)


if __name__ == '__main__':
    main()
