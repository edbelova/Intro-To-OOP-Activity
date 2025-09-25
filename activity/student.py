class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, subject):
        self.classes.append(subject)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        print(f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes")