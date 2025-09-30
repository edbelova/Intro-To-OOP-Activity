from activity.student import Student

def test_new_student():
    # Act
    samara = Student("Bruce Wayne", "5th", ["Math", "Science"])
    #samara = Student( "Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ] )

    # Assert
    assert samara.name == "Bruce Wayne"
    assert samara.grade == "5th"
    assert samara.classes == ["Math", "Science"]
    assert len(samara.classes) == 2

def test_new_student_with_empty_classes():
    # Act
    samara = Student("Bruce Wayne", "5th", [])
    # Assert
    assert samara.name == "Bruce Wayne"
    assert samara.grade == "5th"
    assert samara.classes == []
    assert len(samara.classes) == 0

def test_new_student_with_zero_classes():
    # Act
    samara = Student("Bruce Wayne", "5th")
    # Assert
    assert samara.name == "Bruce Wayne"
    assert samara.grade == "5th"
    assert samara.classes == []
    assert len(samara.classes) == 0

def test_add_new_class_to_exist_classes():
    # Arrange
    samara = Student("Bruce Wayne", "5th", ["Math", "Science"])
    class_name = "Painting"
    # Act
    samara.add_class(class_name)
    # Assert
    assert samara.classes == ["Math", "Science", "Painting"]
    assert len(samara.classes) == 3

def test_add_new_class_to_empty_classes():
    # Arrange
    samara = Student("Bruce Wayne", "5th")
    class_name = "Painting"
    # Act
    samara.add_class(class_name)
    # Assert
    assert samara.classes == ["Painting"]
    assert len(samara.classes) == 1

def test_get_num_classes_for_empty_classes():
    # Arrange
    samara = Student("Bruce Wayne", "5th")
    # Act
    num_of_classes = samara.get_num_classes()
    # Assert
    assert num_of_classes == 0

def test_get_num_classes_return_number_for_not_empty_classes():
    # Arrange
    samara = Student("Bruce Wayne", "5th", ["Math", "Science", "Painting"])
    # Act
    num_of_classes = samara.get_num_classes()
    # Assert
    assert num_of_classes == 3

def test_summary_return_correct_value():
        # Arrange
    samara = Student("Bruce Wayne", "5th", ["Math"])
    # Act
    summary = samara.summary()
    # Assert
    assert summary == "Bruce Wayne is a 5th enrolled in 1 classes"

def test_summary_return_correct_value_for_none_classes():
        # Arrange
    samara = Student("Bruce Wayne", "5th")
    # Act
    summary = samara.summary()
    # Assert
    assert summary == "Bruce Wayne is a 5th enrolled in 0 classes"