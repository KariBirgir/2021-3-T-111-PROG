def main():
    gradebook = {}

    continue_str = "y"
    while continue_str != "n":
        student_email = input("Enter the student email: ")
        student_grade = float(input("Enter the students grade: "))
        add_student_grade(student_email, student_grade, gradebook)
        continue_str = input("Would you like to add another grade (y/n)?: ").lower()
    
    display_grades(gradebook)


def add_student_grade(email, grade, gradebook):
    try:
        gradebook[email].append(grade)
    except KeyError:
        gradebook[email] = [grade]


def display_grades(gradebook):
    for student_email, grades in sorted(gradebook.items()):
        average_grade = sum(grades)/len(grades)
        print(f"{student_email}: {round(average_grade, 2)}")


if __name__ == "__main__":
    main()