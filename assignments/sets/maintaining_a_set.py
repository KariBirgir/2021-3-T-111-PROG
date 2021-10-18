INPUT_MESSAGE = "Enter a word to add to the set: "


def main():
    input_set = set()
    # New feature in Python 3.8, called the walrus operator, allows you to assign a variable and compare it inline.
    while (user_input := input(INPUT_MESSAGE)) != "q":
        input_set.add(user_input)
        print(" ".join(sorted(input_set)))
        print(f"The size of the set is: {len(input_set)}")


if __name__ == "__main__":
    main()