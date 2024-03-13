import math
import numpy as np
import curses
class Student:
    def __init__(self, s_id, s_name, s_dob):
        self.s_id = s_id
        self.s_name = s_name
        self.s_dob = s_dob

class Course:
    def __init__(self, c_id, c_name):
        self.c_id = c_id
        self.c_name = c_name

class Course_selection: 
    @staticmethod                                                                      
    def choose_course(courses):
        print("Select course ID: ")
        for course in courses:
            print(f"ID: {course.c_id}, Name: {course.c_name}")
        chosen_course_id = int(input("Enter the ID of the course you want to choose: "))
        return chosen_course_id

    @staticmethod
    def s_mark(students, course):
        marks = []
        for student in students:
            mark = float(input(f"Input mark of student {student.s_name}: "))
            #Use math module to round-down student scores to 1-digit decimal upon input, floor()
            rounded_mark = math.floor(mark * 10)/10
            marks.append((course.c_id, course.c_name, student.s_id, student.s_name, rounded_mark))
        return marks

#Use numpy module and its array to
#Add function to calculate average GPA for a given student
def calculate_average_gpa(marks):
    return np.mean(marks)

#Weighted sum of credits and marks
def weighted_sum(credits, marks):
    return np.sum(credits * marks)

#Sort student list by GPA descending
def sort_students_by_gpa(students):
    gpas = np.array([student.gpa for student in students])
    sorted_indices = np.argsort(gpas)[::-1]
    sorted_students = [students[i] for i in sorted_indices]
    return sorted_students

#Display the sorted student list using curses
def display_student_list(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "Sorted Student List by GPA (Descending):")
    for i, student in enumerate(students):
        stdscr.addstr(i + 1, 0, f"{student.s_name} - GPA: {student.gpa:.2f}")
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    students = []  #Initialize a list to store student objects
    courses = []   #Initialize a list to store course objects

    #Input student information
    s_number = int(input("Input number of students: "))
    for _ in range(s_number):
        s_id = input("Input student ID: ")
        s_name = input("Input student name: ")
        s_dob = input("Input student DoB: ")
        student = Student(s_id, s_name, s_dob)
        students.append(student)

    #Input course information
    c_number = int(input("Input number of courses: "))
    for _ in range(c_number):
        c_id = input("Input course ID: ")
        c_name = input("Input course name: ")
        course = Course(c_id, c_name)
        courses.append(course)

    choice = -1
    marks = []

    while choice != 0:
        print("1. Select a course and input student marks for the chosen course")
        print("2. Calculate GPA for each student, sort students by GPA then display the sorted student list")
        print("0. Exit")
        print("Enter your choice: ")
        choice = int(input())

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
            display_student_list(stdscr, sorted_students)
        elif choice == 0:
            print("Exiting...")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    curses.wrapper(main)