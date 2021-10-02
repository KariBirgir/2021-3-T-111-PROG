def main():
    a_str = input("Enter a string: ")
    list_of_indexes = input("Enter indices seperated by space: ").split()

    for index in list_of_indexes:
        try:
            print(f"{index}: {a_str[int(index)]}")
        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
