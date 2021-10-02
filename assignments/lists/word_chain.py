def main():
    input_list = []
    criteria_list = []
    continuous_input_to_list(input_list, criteria_list)

    display_results(input_list, criteria_list)


def continuous_input_to_list(input_list, criteria_list):
    PROMPT = "Enter a word to be added to the list: "
    user_input = input(PROMPT)
    while user_input != "x":
        input_list.append(user_input)
        add_criteria(user_input, criteria_list)
        user_input = input(PROMPT)


def add_criteria(user_input, criteria_list):
    try:
        if (
            criteria_list[-1][-1] == user_input[0]
        ):  # Last letter from the chain == first letter from user
            criteria_list.append(user_input)
    except IndexError:
        criteria_list.append(user_input)


def display_results(input_list, criteria_list):
    print(input_list)
    for item in criteria_list:
        print(item)


if __name__ == "__main__":
    main()
