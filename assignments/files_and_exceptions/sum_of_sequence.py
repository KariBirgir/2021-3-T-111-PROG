def main():
    input_sequence = input("Enter in a sequence of numbers seperated by space: ")

    print(sum_sequence(input_sequence))

def sum_sequence(a_str):
    sum_num = 0
    for word in a_str.split():
        try:
            sum_num += int(word)
        except ValueError:
            pass
    return sum_num

if __name__ == "__main__":
    main()