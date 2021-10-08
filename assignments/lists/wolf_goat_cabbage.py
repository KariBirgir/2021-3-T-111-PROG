def main():
    left_side = ["w", "g", "c"]
    right_side = []
    is_left = True
    display_state(left_side, right_side, is_left)

    while len(right_side) < 3 and not has_lost(left_side, right_side, is_left):
        choice = get_user_choice(left_side, right_side, is_left)
        if choice != "e":
            move_choice(left_side, right_side, is_left, choice)
        is_left = not is_left
        display_state(left_side, right_side, is_left)

    if len(right_side) == 3:
        print("You solved the puzzle!")
    else:
        print_losing_message(left_side, right_side, is_left)


def display_state(left_side, right_side, is_left):
    print("You are on the left side." if is_left else "You are on the right side.")
    print(f"{' '.join(left_side)} | {' '.join(right_side)}")


def has_lost(left_side, right_side, is_left):
    opposite_site = right_side if is_left else left_side
    if "w" in opposite_site and "g" in opposite_site:
        return True
    if "g" in opposite_site and "c" in opposite_site:
        return True
    return False


def get_user_choice(left_side, right_side, is_left):
    PROMPT = "What would you like to take over the river? (w/g/c/e): "
    choice = input(PROMPT).lower()

    while not valid_user_choice(left_side, right_side, is_left, choice):
        print("Not a valid choice!")
        choice = input(PROMPT).lower()

    return choice


def valid_user_choice(left_side, right_side, is_left, choice):
    return (
        is_left and choice in left_side
        or not is_left and choice in right_side
        or choice == "e"
    )


def move_choice(left_side, right_side, is_left, choice):
    if is_left:
        left_side.remove(choice)
        right_side.append(choice)
    else:
        right_side.remove(choice)
        left_side.append(choice)


def print_losing_message(left_side, right_side, is_left):
    opposite_site = right_side if is_left else left_side
    if "w" in opposite_site and "g" in opposite_site:
        print("The wolf ate the goat.")
    elif "g" in opposite_site and "c" in opposite_site:
        print("The goat ate the cabbage.")


if __name__ == "__main__":
    main()
