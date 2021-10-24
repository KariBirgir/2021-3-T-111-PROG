def main():
    chemical_eq_1 = input("Input a chemical equation: ")
    chemical_eq_2 = input("Input another chemical equation: ")

    chemical_eq_set_1 = get_chemical_eq_set_from_string(chemical_eq_1)
    chemical_eq_set_2 = get_chemical_eq_set_from_string(chemical_eq_2)
    
    intersection = chemical_eq_set_1.intersection(chemical_eq_set_2)
    print(", ".join(sorted(intersection)))


def get_chemical_eq_set_from_string(chemical_eq_str):
    chemical_eq_set = set()
    while chemical_eq_str:
        if chemical_eq_str[0].isalpha():
            chemical_eq_str = add_element_to_set(chemical_eq_str, chemical_eq_set)
        else:
            chemical_eq_str = chemical_eq_str[1:]
    return chemical_eq_set


def add_element_to_set(chemical_eq_str, chemical_eq_set):
    try:
        if chemical_eq_str[1].islower():
            chemical_eq_set.add(chemical_eq_str[:2])
            chemical_eq_str = chemical_eq_str[2:]
        else:
            raise IndexError
    except IndexError:
        chemical_eq_set.add(chemical_eq_str[0])
        chemical_eq_str = chemical_eq_str[1:]
    return chemical_eq_str


if __name__ == "__main__":
    main()
