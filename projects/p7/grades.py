INVALID_MSG = "Invalid file name"
END_STR = " | "

def main():
    project_file_name = input("Project file name: ")
    project_file_obj = open_file(project_file_name)
    if project_file_obj is None:
        print(INVALID_MSG)
        return

    project_points = get_project_points(project_file_obj)
    print(project_points)
    
    students_file_name = input("Students file name: ")
    students_file_obj = open_file(students_file_name)
    if students_file_obj is None:
        print(INVALID_MSG)
        return
    
    students_points = get_students_points(students_file_obj)
    print(students_points)
    
    students_points_with_grades = compute_grades(students_points, project_points)
    print(students_points_with_grades)

    display_results(project_points, students_points_with_grades)


def open_file(filename):
    '''Opens the given file, returning its file object if found, otherwise None'''
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None

def get_project_points(project_file_obj):
    '''Returns a tuple of the type (str, list) where the first component is project name and
    the second component a list of integers.
    The given file stream contains a single line with information like "test.py 5 6 3 2 4 5"'''
    line = project_file_obj.read().split()
    project_tuple = get_tuple_from_line(line)
    return project_tuple

def get_tuple_from_line(line_str):
    '''Returns a tuple of the type (str, list) extracted from the given string'''
    name, points = line_str[0], line_str[1:]
    points = [int(point) for point in points]
    return (name, points)

def get_students_points(students_points_file_obj):
    '''Returns a list of tuples of the type (str, list), 
    where the first component is an email and the second component is a list of integers.
    The given file stream contains lines, each of which contains information like "student@ru.is 4 5 3 1 3 4'''
    student_results = []
    for line in students_points_file_obj:
        line = line.strip().split()
        student_tuple = get_tuple_from_line(line)
        student_results.append(student_tuple)
    return student_results

def compute_grades(students_points, project_points):
    '''Computes the grade for each student given the points acquired for each student and the associated point distribution.
    Returns a new list in which the students_points tuples have been extended with the grade.'''

    students_points_with_grades = [(name, points, final_grade(points, project_points[1])) for name, points in students_points]
    return students_points_with_grades

def final_grade(student_points, max_points):
    '''Computes the grade based on the given points acquired by a student and the maximum points possible.'''
    return sum(student_points)/sum(max_points)*10

def display_results(point_dist, student_results):
    name, points = point_dist
    display_row(name, points, 10.0)
    
    for name, points, final in student_results:
        display_row(name, points, final)

def display_row(name, points, final):
    print("{:<20}".format(name), end=END_STR)
    for point in points:
        print(point, end=END_STR)
    print("{:>5.2f}".format(final))

# Main program starts here
if __name__ == "__main__":
    main()