def main():
    # Main program starts here - DO NOT change it
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    a_tuple = list_to_bool_tuple(a_list)
    print(a_tuple)

def list_to_bool_tuple(a_list):
    bool_list = []
    for item in a_list:
        try:
            bool_item = bool(int(item))
        except ValueError:
            bool_item = bool(item)
        bool_list.append(bool_item)
    return tuple(bool_list)

if __name__ == "__main__":
    main()