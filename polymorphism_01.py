class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm sleeping")

    def move(self):
        print("I'm moving")

class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name,age)
        self.breed = breed

    def bark(self):
        print("I'm barking")

    def move(self):
        print("I'm moving with 4 legs")


# instance

dog = Dog("Bob", 6, "Rott")
dog.move()