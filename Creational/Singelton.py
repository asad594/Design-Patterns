#Pattern are basically used to solve the problems which occur 
# during software development.these are like blueprints and 
# ready made cde which we can customize according to our needs.


#Singelton pattern aik asa design pattern jo ensure karta ha ka 
#aik class ka sirf aik hi instance ho or uska global point of 
# access ho. Like teh database and logger class must have only 
# one instance to ensure the integrity of the data and to avoid 
# multiple connections to the database.

#Singelton pattern on the printer functionality 
# is used to ensure that only one instance of the 
# printer class is created and used throughout the application.
# This is important because having multiple instances of the 
# printer class could lead to conflicts and inconsistencies in 
# printing operations.

class Printer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating Printer instance...")
            cls._instance = super(Printer, cls).__new__(cls)
        return cls._instance

    def print_document(self, document):
        print(f"Printing document: {document}")


printer1 = Printer()
printer2 = Printer()

printer1.print_document("Report.pdf")

print(printer1 is printer2)  # True
