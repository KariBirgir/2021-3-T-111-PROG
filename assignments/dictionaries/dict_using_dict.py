def main():
    dictionary_dict = {}

    continue_str = "y"
    while continue_str != "n":
        word = input("Input a word: ")
        dictionary_dict[word] = input(f"Enter the definition for {word}: ")
        continue_str = input("Would you like to add another word and definition (y/n)?: ").lower()

    print(sorted(dictionary_dict.items()))


if __name__ == "__main__":
    main()
