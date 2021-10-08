# DESCRIPTION

"""
Write a function that takes a list L of integers as an argument and uses LIST COMPREHENSION to return the sum
of all prime numbers from the list L.

Hint: In your implementation, you can use some of the list functions discussed on page 349 in the textbook.

You are given the function is_prime(n) to check whether the number n is a prime or not (The function returns a boolean)

The main function and two other functions are given - DO NOT change it.

For example:
Enter elements of list seperated by commas: 1,2,3,4,5,6,7,8,9,10,11
28
"""

# TEMPLATE

"""
from math import sqrt

def main():
    a_list = get_list()
    print(prime_sum(a_list))

# These functions are given, do not change them, you can however call them.
def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def get_list():
    a_list = input("Enter elements of list seperated by commas: ").strip().split(",")
    a_list = [int(number) for number in a_list]
    return a_list

# implement prime_sum(a_list) here below


# main functionality
if __name__ == "__main__":
    main()
"""

# SOLUTION

# radon hal Difficulty : 3.84, although keep in mind that two functions are given, list comprehension is the only challenge in this problem

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
