a_str = input("Enter a string: ")
word_in_str = input("Enter in a substring you want to replace: ")
replacement = input("Enter in a substring you want to replace it with: ")

if word_in_str not in a_str:
    print("Substring is not in the string")
else:
    new_str = ""
    word_len = len(word_in_str)
    i = 0
    while i < len(a_str):
        if a_str[i:i+word_len] == word_in_str:
            new_str += replacement
            i += word_len
        else:
            new_str += a_str[i]
            i += 1
    print(new_str)
