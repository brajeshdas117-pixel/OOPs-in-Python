class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog is barking!")

# instances

dog = Dog()
animal = Animal()

animal.speak()
dog.speak()                        # here the method overriding is performed