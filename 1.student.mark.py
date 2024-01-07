#1. Input functions:
#Input number of students in a class
def s_number():
    return int(input("Input number of students: "))

#Input student information: id, name, DoB
def s_info():
    s_id = (input("Input student ID: "))
    s_name = input("Input student name: ")
    s_dob = input("Input student DoB: ")
    return (s_id, s_name, s_dob)

#Input number of courses
def c_number():
    return int(input("Input number of courses: "))

#Input course information: id, name
def c_info():
    c_id = int(input("Input course ID: "))
    c_name = input("Input course name: ")
    return (c_id, c_name)

#Select a course, input marks for student in this course
def choose_c_id():
    return int(input("Select course ID: "))

def s_mark(students, course):
    c_id, c_name = course
    marks = []
    for student in students:
        mark = float(input(f"Input mark of student {student[1]}: "))
        marks.append((c_id, c_name, student[0], student[1], mark))
    return marks

#2. Listing functions:
#List courses
def c_list(courses):
    print("List of course:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")
     
#List students
def s_list(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def main():
    students = [s_info() for _ in range(s_number())]
    courses = [c_info() for _ in range(c_number())]
    
    s_list(students)
    c_list(courses)

    chosen_course_id = choose_c_id()
    marks = s_mark(students, courses[chosen_course_id-1])

# Show student marks for a given course
    print("Student marks in the chosen course is:")
    print("(Course ID, Course name, Student ID, Student name, Mark)")
    for mark in marks:
        print(mark)

main()