# Builder design pattern aik creational design pattern ha jo 
# allow karta ha ka hum aik complex object ko step by step 
# construct karen.

# Builder pattern aik separate builder class provide karta ha 
# jo step by step object ko construct karne ka process handle 
# karta ha.

#Like agar hum aik car object create karna chahte hain to hum
# car ka engine, wheels, color, model etc. step by step set kar 
# sakte hain aur finally car object ko build kar sakte hain.

class Car:
    def __init__(self):
        self.engine = ""
        self.wheels = ""
        self.color = ""
        self.model = ""

    def show(self):
        print("Car Details")
        print("Engine :", self.engine)
        print("Wheels :", self.wheels)
        print("Color  :", self.color)
        print("Model  :", self.model)


class CarBuilder:

    def __init__(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.engine = engine

    def set_wheels(self, wheels):
        self.car.wheels = wheels

    def set_color(self, color):
        self.car.color = color

    def set_model(self, model):
        self.car.model = model

    def build(self):
        return self.car


#Director class building process ko control karti hai. 
# Ye janti hai kaun se steps kis order mein execute karne hain, 
# lekin isay ye nahi pata hota ke har part internally kaise build 
# ho raha hai. Ye sirf Builder ko instructions deti hai, aur
# Builder final object tayar karta hai.

class Director:

    def construct_car(self, builder):
        builder.set_engine("V8 Engine")
        builder.set_wheels("4 Wheels")
        builder.set_color("Black")
        builder.set_model("BMW X5")


builder = CarBuilder()
director = Director()

director.construct_car(builder)

car = builder.build()
car.show()