def main():
    file_obj = open_file("countries.txt")
    country_suffix = input("Enter a suffix for a country: ")
    count = 0
    for country in file_obj:
        country = country.strip()
        if country.endswith(country_suffix):
            print(country)
            count += 1
        
    print(f"{count} countries with suffix '{country_suffix}'.")
    file_obj.close()

def open_file(file_name):
    return open(file_name, "r")

if __name__ == "__main__":
    main()