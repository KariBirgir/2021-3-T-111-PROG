def main():
    a_list = [3, 9, 5, 1, 6, 8]
    print(f"{a_list = }")
    remove_min_and_max(a_list)
    print(f"{a_list = }")

    b_list = [9, 2, 3, 6, 1, 8, 7]
    c_list = remove_min_and_max_2(b_list)
    print(f"{b_list = }")
    print(f"{c_list = }")


def remove_min_and_max(a_list):
    min_index, max_index = find_min_and_max_index(a_list)
    del a_list[min_index]
    if min_index < max_index:
        max_index -= 1
    del a_list[max_index]


def remove_min_and_max_2(a_list):
    min_index, max_index = find_min_and_max_index(a_list)
    return [
        a_list[i] for i in range(len(a_list)) if (i != min_index and i != max_index)
    ]


def find_min_and_max_index(a_list):
    min_index = 0
    max_index = 0
    for i in range(1, len(a_list)):
        if a_list[min_index] > a_list[i]:
            min_index = i
        if a_list[max_index] < a_list[i]:
            max_index = i
    return min_index, max_index


if __name__ == "__main__":
    main()
