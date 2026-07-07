#Decorator design pattern aik structural design pattern hai jo 
# allow karta ha ka hum existing object ki functionality ko 
# dynamically extend kar saken or change kr sakay functionality 
# by wrapping the object bina uske structure ko modify 

# Decorator design pattern aik structural design pattern hai jo
# object ki functionality ko dynamically extend karne ki
# ijazat deta hai, object ko "wrap" karke — bina uski
# original class ya structure ko modify kiye.

from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def activate(self):
        pass

class BasicPhone(Phone):
    def activate(self):
        return "Phone is ringing"

class PhoneDecorator(Phone):
    def __init__(self, phone):
        self.phone = phone   

    def activate(self):
        return self.phone.activate()

class Flashlight(PhoneDecorator):
    def activate(self):
        return self.phone.activate() + " + Flashlight blinking"

class Ringtone(PhoneDecorator):
    def activate(self):
        return self.phone.activate() + " + Custom Ringtone playing"


phone = BasicPhone()
phone = Flashlight(phone)
phone = Ringtone(phone)

print(phone.activate())