# Composite pattern ek structural design pattern hai jo
# objects ko tree structure mein arrange karne deta hai
# taake part-whole hierarchies represent ho sakein.
# Is se client individual objects aur unke groups
# (compositions) ko same tarah (uniformly) treat kar sakta hai.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def show_details(self):
        pass

class Developer(Employee):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Developer: {self.name}")

class Designer(Employee):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Designer: {self.name}")

class Manager(Employee):
    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def add(self, employee):
        self.subordinates.append(employee)

    def show_details(self):
        print(f"Manager: {self.name}")
        for emp in self.subordinates:
            emp.show_details()  


if __name__ == "__main__":
    dev1 = Developer("Ali")
    designer1 = Designer("Sara")

    team_lead = Manager("Asad")
    team_lead.add(dev1)
    team_lead.add(designer1)

    team_lead.show_details()