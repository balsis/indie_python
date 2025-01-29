class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self._course = 1
        self.__marks = marks or []

    @property
    def average_marks(self):
        return sum(self.__marks) / len(self.__marks)


student = Student(name="Kevin")
print(student.average_marks)