def main():
    a_str = input("Enter a string: ")
    index = input("Enter an index: ")
    char_at_index = get_char_at_index(a_str, index)
    if char_at_index:
        print(f"The character at index {index} is '{char_at_index}'.")

def get_char_at_index(string, index):
    try:
        return string[int(index)]
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Index not an integer.")
    # this line doesnt need to be here, but is here for clarity
    return None

if __name__ == "__main__":
    main()