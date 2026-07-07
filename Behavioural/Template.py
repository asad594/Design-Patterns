#Template aik behaviural design pattern ha jis ma hum jitnay bhi
#same steps hain un ko aik class (template) ma define kartay or 
#subclaasees us ko use karti ha or ko functiona jo different ha 
# woh subclass ma define hota ha. Ye pattern code reusability 
# aur consistency provide karta ha.


from abc import ABC, abstractmethod

class Beverage(ABC):

    def prepare(self):
        self.boil_water()
        self.add_main_ingredient()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def add_main_ingredient(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

class Tea(Beverage):
    def add_main_ingredient(self):
        print("Adding tea leaves")

    def add_condiments(self):
        print("Adding milk")

class Coffee(Beverage):
    def add_main_ingredient(self):
        print("Adding coffee powder")

    def add_condiments(self):
        print("Adding sugar")


print("Making Tea:")
tea = Tea()
tea.prepare()

print("\nMaking Coffee:")
coffee = Coffee()
coffee.prepare()