from activity.student import Student
from activity.comparison import get_student_with_more_classes

def test_compare_numbers():
    # Arrange
    hsiang_ting = Student("Hsiang-Ting", "5th", ["Math", "Science"])
    geetha = Student("Geetha", "5th", ["Math", "Science", "Painting"])
    # Act
    most_classes_student = get_student_with_more_classes(hsiang_ting, geetha)
    # Assert
    assert most_classes_student == geetha

def test_compare_numbers_tie():
    # Arrange
    hsiang_ting = Student("Hsiang-Ting", "5th", ["Math", "Science"])
    geetha = Student("Geetha", "5th", ["Math", "Science"])
    # Act
    most_classes_student = get_student_with_more_classes(hsiang_ting, geetha)
    # Assert
    assert most_classes_student == hsiang_ting

def test_compare_numbers_with_no_classes_for_one_student():
    # Arrange
    hsiang_ting = Student("Hsiang-Ting", "5th")
    geetha = Student("Geetha", "5th", ["Math", "Science"])
    # Act
    most_classes_student = get_student_with_more_classes(hsiang_ting, geetha)
    # Assert
    assert most_classes_student == geetha