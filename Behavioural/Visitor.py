#Visitor ek behavioral design pattern hai jo tumhe kisi object 
# structure (classes ke group) par naye operations add karne 
# deta hai bina un classes ko modify kiye. Ye operation ko ek 
# alag Visitor object mein encapsulate karta hai, jo har element
# ko "visit" karta hai aur us par apna logic apply karta hai  
# is tarah data structure (elements) aur operations (algorithms) 
# ko separate kar deta hai.


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Dog(Animal):
    def accept(self, visitor):
        visitor.visit_dog(self)

class Cat(Animal):
    def accept(self, visitor):
        visitor.visit_cat(self)


class AnimalVisitor(ABC):
    @abstractmethod
    def visit_dog(self, dog):
        pass
    @abstractmethod
    def visit_cat(self, cat):
        pass

class SoundVisitor(AnimalVisitor):
    def visit_dog(self, dog):
        print("Dog says: Woof!")

    def visit_cat(self, cat):
        print("Cat says: Meow!")

class FoodVisitor(AnimalVisitor):
    def visit_dog(self, dog):
        print("Dog eats: Bones")

    def visit_cat(self, cat):
        print("Cat eats: Fish")


animals = [Dog(), Cat()]

print("-- Sounds --")
sound_visitor = SoundVisitor()
for animal in animals:
    animal.accept(sound_visitor)

print("\n-- Food --")
food_visitor = FoodVisitor()
for animal in animals:
    animal.accept(food_visitor)