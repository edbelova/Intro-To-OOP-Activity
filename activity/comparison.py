# add your get_student_with_more_classes function here!


# This is the solution for the case when we need to compare an unknown number of students by using *args

# def get_student_with_more_classes(*students):
#     most_classes_student = students[0]
#     for student in students[1:]:
#         if student.get_num_classes() > most_classes_student.get_num_classes():
#             most_classes_student = student
#     return most_classes_student.name