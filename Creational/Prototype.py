# Prototype paattern aik creational design pattern ha jo aik 
# object ka clone create karne ka tareeqa provide karta ha bina 
# ye specify kiye ke ye object kaun si class ka ha.
# Agr hmay object ma koi changes karni ho to hum easily us
#  object ka clone create kar sakte hain or us may changes kar 
# sakte hain bina original object ko effect kiye.

#like agar hmare pass aik car object ha or hmay uska clone 
# create karna ha to hum easily car object ka clone create kar 
# sakte hain or us may changes kar sakte hain bina original car
#  object ko effect kiye.

import copy

class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def show(self):
        print("Model :", self.model)
        print("Color :", self.color)

car1 = Car("BMW X5", "Black")

car2 = car1.clone()

car2.color = "Red"

print("Original Car")
car1.show()

print("\nCloned Car")
car2.show()