#Bridge pattern aik structural design pattern hai jo allow 
# karta ha ka hum Abstraction(hiding unecessary details) or 
# implementation ko alag rakhein. Ye pattern ek bridge provide 
# karta hai jo abstraction ko implementation ke sath connect 
# karta hai. Taqay dono ko independently modify kiya ja sakay.

from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class RedColor(Color):
    def fill(self):
        return "Red"

class GreenColor(Color):
    def fill(self):
        return "Green"

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color   

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print(f"Circle filled with {self.color.fill()}")

class Square(Shape):
    def draw(self):
        print(f"Square filled with {self.color.fill()}")


if __name__ == "__main__":
    red_circle = Circle(RedColor())
    green_square = Square(GreenColor())

    red_circle.draw()     
    green_square.draw()   