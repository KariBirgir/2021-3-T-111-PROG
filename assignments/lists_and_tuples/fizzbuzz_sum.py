def main():
    max_num = int(input("What should max_num be?: "))
    print(fizzbuzz_sum(max_num))

def fizzbuzz_sum(max_num):
    return sum([i for i in range(max_num) if i % 3 == 0 and i % 5 == 0])
    
# Main program starts here - DO NOT change it
if __name__ == "__main__":
    main()
