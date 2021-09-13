items = input("Enter any items seperated by space: ")

for item in items.split():
    count = int(input(f"Repeat {item} how many times?: "))
    print((item + " ")*count)