class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = 0  
        self.set_marks(marks)  

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks entered. Marks must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Student(Name = {self.__name}, Marks = {self.__marks})"


student1 = Student("David", 85)
student2 = Student("John", 92)

print(student1)
print(student2)


student1.set_marks(95)

print("\nMarks of Student 1 after updating:")
print(student1)

student1.set_marks(-1)

print("\nCurrent marks:", student1.get_marks())




