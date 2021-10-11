MAX = 1000000


def main():
    for i in range(10, MAX + 1):
        if has_property(i):
            print(i)


def has_property(number):
    for i in range(2, number_of_digits(number) + 1):
        if not is_permutation_of_same_digits(number, number * i):
            return False
    return True


def number_of_digits(number):
    return len(str(number))


def is_permutation_of_same_digits(num1, num2):
    return sorted_digits(num1) == sorted_digits(num2)


def sorted_digits(number):
    return sorted(str(number))


if __name__ == "__main__":
    main()
