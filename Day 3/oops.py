"""
class Cat:
    pass 
nabi = Cat()
print(nabi)


class Cat:
    def meow(self):
        print("meow")
    
nabi = Cat()
nabi.meow()
"""

"""
class Circle:                 # creating a class (blueprint for objects)
    PI = 3.14                # class variable (same for all Circle objects)

    def __init__(self, name, radius):   # constructor runs automatically when object is created
        self.__name = name              # stores "name" inside THIS object (name-mangled)
        self.__radius = radius          # stores "radius" inside THIS object (name-mangled)


c1 = Circle("C1", 5)         # creating object c1
                             # Python internally calls:
                             # Circle.__init__(c1, "C1", 5)

print("Attributes of c1:", c1.__dict__)
# __dict__ shows ALL data stored inside the object
# here Python stores private variables in mangled form:
# {'_Circle__name': 'C1', '_Circle__radius': 5}


print("Name:", c1._Circle__name)
# accessing "name" directly from object memory
# Python renamed __name → _Circle__name internally

print("Radius:", c1._Circle__radius)
# accessing "radius" directly from object memory
# Python renamed __radius → _Circle__radius internally

"""

"""
class Dog:
   
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name, "Says Woof Woof")

        
my_dog = Dog("Bingo")
my_dog.bark()
my_dog = Dog("Scooby")
my_dog.bark()
"""


class student:
    def __init__ (self, name, student_id, eng_quiz, math_quiz, science_quiz):
        self.name = name
        self.student_id=student_id
        self.eng_quiz= eng_quiz
        self.math_quiz= math_quiz
        self.science_quiz= science_quiz

name = input("Enter name: ")
student_id = input("Enter student id")
eng_quiz = input("Enter eng_quiz:")
math_quiz = input("Enter maths quiz:")
science_quiz = input("Enter science quiz")
#incomplete... will solve





