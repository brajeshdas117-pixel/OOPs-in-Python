# Create a student class with aattributes name, age and gender.

class Student:

    # methods

    def __init__(self, name: str, age: int, gender: str):

        # Attributes

        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1 = Student("Brajesh", 23, "Male")
print(s1.display_info())