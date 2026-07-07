#The factory pattern aik creational design pattern ha handles 
# the creation of object it has a factory method which is 
# responsible for creating the object without specifying 
# the exact class of the object to be created. 
# and return the object of that class based on the user input 
# or configuration. 

# Like we have three classes of payments methods
#Easypaisa jazzcash credit card and we have a factory method which 
# will return the object of the payment method class based on the user input.

class EasyPaisa:
    def pay(self, amount):
        print(f"Paid Rs. {amount} using EasyPaisa.")


class JazzCash:
    def pay(self, amount):
        print(f"Paid Rs. {amount} using JazzCash.")


class CreditCard:
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Credit Card.")


class PaymentFactory:

    def get_payment_method(self, method):

        if method.lower() == "easypaisa":
            return EasyPaisa()

        elif method.lower() == "jazzcash":
            return JazzCash()

        elif method.lower() == "creditcard":
            return CreditCard()

        else:
            return None


factory = PaymentFactory()

method = input("Enter Payment Method (EasyPaisa/JazzCash/CreditCard): ")
amount = float(input("Enter Amount: "))

payment = factory.get_payment_method(method)

if payment:
    payment.pay(amount)
else:
    print("Invalid Payment Method")