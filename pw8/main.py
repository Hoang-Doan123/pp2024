import curses
import input
from input import get_input
from input import get_int_input
from domains.student import Student
from domains.course import Course
from domains.course_selection import Course_selection
from gpas import calculate_average_gpa
from gpas import sort_students_by_gpa
from output import display_sorted_student_list
from picklefile import write_to_file
from picklefile import pickle_data_in_background
import os
import zipfile

def main():
    
    students = []  #Initialize a list to store student objects
    courses = []   #Initialize a list to store course objects

    #Input student information
    s_number = int(get_int_input("Input number of students: "))
    for _ in range(s_number):
        s_id = get_int_input("Input student ID: ")
        s_name = get_input("Input student name: ")
        s_dob = get_input("Input student DoB: ")
        student = Student(s_id, s_name, s_dob)
        students.append(student)
    #Write student info to students.txt after finishing input
    write_to_file(students, "students.txt")

    #Input course information
    c_number = int(get_int_input("Input number of courses: "))
    for _ in range(c_number):
        c_id = get_int_input("Input course ID: ")
        c_name = get_input("Input course name: ")
        course = Course(c_id, c_name)
        courses.append(course)
    #Write course info to courses.txt after finishing input
    write_to_file(courses, "courses.txt")

    choice = -1
    marks = []

    while choice != 0:
        print("1. Select a course and input student marks for the chosen course")
        print("2. Calculate GPA for each student, sort students by GPA then display the sorted student list")
        print("0. Exit")
        print("Enter your choice: ")
        choice = int(get_int_input(message = ""))

        if choice == 1:
            # Select a course
            chosen_course_id = Course_selection.choose_course(courses)
            # Input student marks for the chosen course
            marks = Course_selection.s_mark(students, courses[chosen_course_id-1])
            
        elif choice == 2:
            # Calculate GPA for each student
            for student in students:
                student_marks = [mark[4] for mark in marks if mark[2] == student.s_id]
                student.gpa = calculate_average_gpa(student_marks)
            # Sort students by GPA
            sorted_students = sort_students_by_gpa(students)
            # Display the sorted student list using curses
            display_sorted_student_list(sorted_students)
        elif choice == 0:
            print("Exiting...")
        else:
            print("Invalid choice. Try again.")

#Select a compression method
compression_method = "zip"  

if compression_method == "zip":
    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
    
    with zipfile.ZipFile("data.zip", "w") as zipf:
        for file in files_to_compress:
            zipf.write(file)

    if os.path.exists('data.zip'):
        with zipfile.ZipFile("data.zip", "r") as zipf:
            zipf.extractall()

    #Pickle data in the background thread
    pickle_data_in_background(Student, "students.pickle")
    pickle_data_in_background(Course, "courses.pickle")

main()
