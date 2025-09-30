class Student:
    def __init__(self, name, grade, classes = None):
        self.name = name
        self.grade = grade
        self.classes = [] if classes is None else classes
        #self.classes = classes

    def add_class(self, subject):
        self.classes.append(subject)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"