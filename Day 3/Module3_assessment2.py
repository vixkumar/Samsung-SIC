class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = 0  
        self.set_salary(salary)  

    def set_salary(self, salary):
        if 0 < salary:
            self.__salary = salary
        else:
            print("Invalid salary entered")

    def get_salary(self):
        return self.__salary

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Employee(Name = {self.__name}, Marks = {self.__salary})"


employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 65000)

print(employee1)
print(employee2)


employee1.set_salary(550000)

print("\nMarks of Employee 1 after updating:")
print(employee1)

employee1.set_salary(-1)

print("\nCurrent marks:", employee1.get_salary())