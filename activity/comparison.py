# from student import student

# def get_student_with_more_classes(*students):
#     most_classes_student = students[0]
#     for student in students[1:]:
#         if student.get_num_classes() > most_classes_student.get_num_classes():
#             most_classes_student = student
#     return most_classes_student

def get_student_with_more_classes(student, other_student):
    if student.get_num_classes() >= other_student.get_num_classes():
        most_classes_student = student
    else:
        most_classes_student = other_student

    return most_classes_student