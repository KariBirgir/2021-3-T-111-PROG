NAME_PROMPT = "Enter your name: "
AGE_PROMPT = "Enter your age: "

def main():
    name = get_name()
    age = get_age()
    print(f"Hello {name}, age {age}.")

def get_name():
    name = input(NAME_PROMPT)
    while not valid_name(name):
        print("Please enter a valid name.")
        name = input(NAME_PROMPT)
    return name

def valid_name(string):
    return string and string.replace(" ", "").isalpha()

def get_age():
    age = input(AGE_PROMPT)
    while not validate_age(age):
        age = input(AGE_PROMPT)
    return age

def validate_age(string):
    try:
        age = int(string)
        if 0 <= age <= 125:
            return True
        else:
            print("Age is not in range!")
    except ValueError:
        print("Please enter an integer.")
    return False

if __name__ == "__main__":
    main()