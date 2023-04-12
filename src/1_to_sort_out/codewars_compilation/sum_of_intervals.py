# there are four cases:
# - int1[0] <= int2[0] and int1[1] >= int2[1] -> do not count
# - int1[0] <= int2[0] <= int1[1] and int1[1] <= int2[1] -> len(int1) - ((int2[1] - int1[0]))
# - int1[0] >= int2[0] and int1[1] >= int2[1] -> len(int1) - ((int2[1] - int1[0]))


def sum_of_intervals(intervals):
    interval_sum = 0
    for i, interval_to_compare in enumerate(intervals):
        for j, interval in enumerate(intervals):
            if j == i:
                continue
            if interval[0] >= interval_to_compare[0]:
                pass
        interval_sum += interval_to_compare[1] - interval_to_compare[0]
    return interval_sum

