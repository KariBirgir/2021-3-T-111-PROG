from string import punctuation

def main():
    a_sent = input("Enter in a sentence: ")
    b_sent = input("Enter in another sentence: ")

    a_sent_dict = string_to_dict(a_sent)
    b_sent_dict = string_to_dict(b_sent)

    if a_sent_dict == b_sent_dict:
        print(f"{a_sent} is an anagram of {b_sent}.")
    else:
        print(f"{a_sent} is not an anagram of {b_sent}.")


def string_to_dict(string):
    string_dict = {}
    for letter in string.lower():
        if letter not in punctuation + " ":
            add_letter_to_dict(letter, string_dict)
    return string_dict


def add_letter_to_dict(letter, string_dict):
    try:
        string_dict[letter] += 1
    except KeyError:
        string_dict[letter] = 1


if __name__ == "__main__":
    main()
