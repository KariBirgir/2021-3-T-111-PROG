def main():
    file_name = input("Enter a filename: ")
    file_obj = open(file_name, "r")
    numbers = get_numbers_from_file(file_obj)
    print(sorted(numbers))


def get_numbers_from_file(file_obj):
    numbers = []
    for line in file_obj:
        word_list = line.strip().split()
        for word in word_list:
            if word.isdigit():
                numbers.append(int(word))
    return numbers


if __name__ == "__main__":
    main()