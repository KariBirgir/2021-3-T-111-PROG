UNION_MESSAGE = "The two files have {} words in common."
SYM_DIFF_MESSAGE = "There are {} words that are only in either file but not both."
DIFF_MESSAGE = "There are {} words that only appear in the first file."

def main():
    filename1 = input("Enter the path to the first file: ")
    filename2 = input("Enter the path to the second file: ")

    words1 = read_words(filename1)
    words2 = read_words(filename2)

    shared_words = get_intersection(words1, words2)
    symm_diff_words = get_symmetric_difference(words1, words2)
    diff_words = get_difference(words1, words2)
    print_metric(shared_words, UNION_MESSAGE)
    print_metric(symm_diff_words, SYM_DIFF_MESSAGE)
    print_metric(diff_words, DIFF_MESSAGE)

def read_words(filename):
    words_set = set()
    with open(filename, "r") as file:
        for line in file:
            for word in line.strip().split():
                words_set.add(word)
    return words_set
        

def get_intersection(set1, set2):
    return set1.intersection(set2)

def get_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def get_difference(set1, set2):
    return set1 - set2

def print_metric(words, message):
    print(message.format(len(words)))
    print("These words are as follows: ", end = "")
    for word in sorted(words):
        # if the word is the last word in the sorted list
        if word == sorted(words)[-1]:
            print(f"and {word}", end=".")
        else:
            print(word, end=", ")
    print()


if __name__ == "__main__":
    main()