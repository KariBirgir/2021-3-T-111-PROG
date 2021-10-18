def main():
    file_name = input("Enter a filename: ")
    file_obj = open_file(file_name)
    if file_obj:
        country_length_dict = make_country_length_dict_from_file(file_obj)
        file_obj.close()

        user_len = int(input("Enter the length you want to search for: "))
        try:
            print(", ".join(country_length_dict[user_len]))
        except KeyError:
            print(f"No country name of length {user_len} exists.")
    else:
        print("Invalid file!")


def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None


def make_country_length_dict_from_file(file_obj):
    country_length_dict = {}
    for line in file_obj:
        country = line.strip()
        try:
            country_length_dict[len(country)].append(country)
        except KeyError:
            country_length_dict[len(country)] = [country]
    return country_length_dict


if __name__ == "__main__":
    main()
