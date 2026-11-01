from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass 

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, length: int, breadth: int):
        self.lenght = length
        self.breadth = breadth

    def area(self):
        print(self.lenght * self.breadth)

    def perimeter(self):
        print(2 * (self.lenght + self.breadth))


r = Rectangle(5, 3)
r.area()
r.perimeter()