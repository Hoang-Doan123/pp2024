import input
import math
from input import get_int_input
from input import get_float_input
from input import round_down_decimal
from createfile import write_to_file

class Course_selection: 
    @staticmethod                                                                      
    def choose_course(courses):
        print("Select course ID: ")
        for course in courses:
            print(f"ID: {course.c_id}, Name: {course.c_name}")
        chosen_course_id = int(get_int_input("Enter the ID of the course you want to choose: "))
        return chosen_course_id

    @staticmethod
    def s_mark(students, course):
        marks = []
        for student in students:
            mark = float(get_float_input(f"Input mark of student {student.s_name}: "))
            #Use math module to round-down student scores to 1-digit decimal upon input, floor()
            rounded_mark = round_down_decimal(mark)
            marks.append((course.c_id, course.c_name, student.s_id, student.s_name, rounded_mark))
        #Write marks to marks.txt after finishing input
        write_to_file("marks.txt", marks)
        return marks