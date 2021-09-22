def main():
    file_name = input("Enter the filename: ")
    file_obj = open_file(file_name)
    for line in file_obj:
        line = line.strip()
        for word in line.split():
            print(word[::-1], end=" ")
        print()
    file_obj.close()

def open_file(file_name):
    return open(file_name, "r")

if __name__ == "__main__":
    main()