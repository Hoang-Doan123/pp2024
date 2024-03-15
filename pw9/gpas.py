import numpy as np
#Add function to calculate average GPA for a given student
def calculate_average_gpa(marks):
    arr = np.array(marks)
    gpa = np.mean(arr)
    return gpa

#Weighted sum of credits and marks
def weighted_sum(credits, marks):
    return np.sum(credits * marks)

#Sort student list by GPA descending
def sort_students_by_gpa(students):
    gpas = np.array([student.gpa for student in students])
    sorted_indices = np.argsort(gpas)[::-1]
    sorted_students = [students[i] for i in sorted_indices]
    return sorted_students