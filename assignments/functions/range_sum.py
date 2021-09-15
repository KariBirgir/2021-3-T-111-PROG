def sum_of_range(start, end, step):
    sum_num = 0
    for i in range(start, end + 1, step):
        sum_num += i
    return sum_num