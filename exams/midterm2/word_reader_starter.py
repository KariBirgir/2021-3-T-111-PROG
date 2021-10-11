def main(): 
    file_name = input("Enter filename: ")
    file_stream = open_file(file_name)
    if file_stream is not None:
        # your code goes here
    else:
        print("File {} not found!".format(file_name))

# Your functions appear here

    
# Main program starts here
if __name__ == "__main__":
    main()