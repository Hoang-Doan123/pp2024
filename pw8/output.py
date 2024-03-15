def display_sorted_student_list(students):
    print("Sorted Student List by GPA (Descending):")
    for student in students:
        print(f"{student.s_name} - GPA: {student.gpa:.2f}")