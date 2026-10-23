# Inherintance

# parent class

class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

# Child class

class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name,age)                          # super(), just call the attributes of parent class
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display_info(self):
        print(f"name is {self.name}, age is {self.age}")

dog = Dog("Happy", 4, "German")
