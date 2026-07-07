#Strategy ek behavioral design pattern hai jo algorithms ki ek 
# family ko define karta hai, har algorithm ko alag class mein 
# encapsulate karta hai, aur unhe interchangeable banata hai  
# taake client runtime pe khud decide kar sake konsi strategy 
# (algorithm) use karni hai, bina us class ko modify kiye jo 
# algorithm use kar rahi hai.


#State ek behavioral design pattern hai jo kisi object ko uski 
# internal state change hone par apna behavior change karne 
# deta hai — is tarah ke lagta hai jaise object ne apni class 
# hi badal li ho. Har state ko alag class mein represent kiya 
# jata hai, aur object khud apni state ke hisab se agli state 
# pe automatically transition karta hai.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class EasyPaisaPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using EasyPaisa")

class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy   # runtime pe change ho sakti hai

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


cart = ShoppingCart(CreditCardPayment())
cart.checkout(1500)

cart.set_strategy(EasyPaisaPayment())   # strategy change kar di
cart.checkout(800)