
from math import sqrt


def main():
    a_list = get_list()
    print(prime_sum(a_list))


def get_list():
    a_list = input("Enter elements of list seperated by commas: ").strip().split(",")
    a_list = [int(number) for number in a_list]
    return a_list


def prime_sum(a_list):
    return sum([number for number in a_list if is_prime(number)])


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    main()
