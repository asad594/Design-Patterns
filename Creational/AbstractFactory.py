#Abstract factory pattern aik creational design pattern ha jo 
# allow karta ha to produce the families of related or 
# dependent objects without specifying their concrete classes.

#Abstract factory deign pattern create the family of objaect at 
# the same time — matlab objects aapas mein connected/matching
# hote hain. 

#If the user chooses the Normal Shape Factory:
#Normal Circle
#Normal Rectangle
#Both shapes belong to the Normal Shapes family.
#If the user chooses the Rounded Shape Factory:
#Rounded Circle
#Rounded Rectangle
#Both shapes belong to the Rounded Shapes family and match each other.


class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")


class RoundedCircle(Shape):
    def draw(self):
        print("Drawing a Rounded Circle")


class RoundedRectangle(Shape):
    def draw(self):
        print("Drawing a Rounded Rectangle")


class ShapeFactory:
    def get_shape(self, shape):
        pass


class NormalShapeFactory(ShapeFactory):

    def get_shape(self, shape):
        if shape.lower() == "circle":
            return Circle()
        elif shape.lower() == "rectangle":
            return Rectangle()
        else:
            return None


class RoundedShapeFactory(ShapeFactory):

    def get_shape(self, shape):
        if shape.lower() == "circle":
            return RoundedCircle()
        elif shape.lower() == "rectangle":
            return RoundedRectangle()
        else:
            return None


class FactoryProducer:

    @staticmethod
    def get_factory(factory_type):

        if factory_type.lower() == "normal":
            return NormalShapeFactory()

        elif factory_type.lower() == "rounded":
            return RoundedShapeFactory()

        else:
            return None


factory_type = input("Enter Factory (Normal/Rounded): ")

factory = FactoryProducer.get_factory(factory_type)

if factory:
    shape_name = input("Enter Shape (Circle/Rectangle): ")
    shape = factory.get_shape(shape_name)

    if shape:
        shape.draw()
    else:
        print("Invalid Shape")
else:
    print("Invalid Factory")