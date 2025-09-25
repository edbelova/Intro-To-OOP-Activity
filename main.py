from activity.student import Student
from activity.comparison import get_student_with_more_classes

# first instance
samara = Student( "Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ] )

samara.add_class("Painting")  # => [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition", "Painting" ]
print(samara.classes)

# samara.get_num_classes() # => 7
print(samara.get_num_classes())

samara.summary()  # => "Samara is a junior enrolled in 7 classes"

# second instance
claire = Student( "Claire", "freshman", [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science" ] )

claire.add_class("Painting")  # => [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science", "Painting" ]
print(claire.classes)

# claire.get_num_classes()  # => 6
print(claire.get_num_classes())

claire.summary()  # => "Claire is a freshman enrolled in 6 classes"

# function
print(get_student_with_more_classes(claire, samara))  # => samara