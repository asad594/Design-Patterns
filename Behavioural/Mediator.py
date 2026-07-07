#Mediator pattern aik behavioral design pattern jo objects ka 
# beech communication ka liya use hota ha agr object directly 
# aik dosray sa communicate karay to ye tightly coupled ho jata
#  ha or agar aik object change hota to dosray object bhi effect
#  hotay ha isi liya aik Mediator pattern aik mediator object ka
#  use karta ha jo objects ka beech communication ko manage karta
#  ha or objects ko loosely coupled rakhta ha.

#Har object dosray object ka sath communicate karne ki bajaye 
# mediator object ka use karta ha jo communication ko manage 
# karta ha. Ye pattern aik central hub provide karta ha jahan 
# objects apni requests aur responses ko mediator ke through 
# pass karte hain, is tarah se objects directly aik dosray sa 
# communicate nahi karte.

class Mediator:
    def __init__(self):
        self.checkbox_checked = False

    def notify(self, sender, event):
        if sender == "checkbox" and event == "toggle":
            if self.checkbox_checked:
                print("TextBox enabled")
            else:
                print("TextBox disabled")

class Checkbox:
    def __init__(self, mediator):
        self.mediator = mediator

    def toggle(self):
        self.mediator.checkbox_checked = not self.mediator.checkbox_checked
        print("Checkbox toggled")
        self.mediator.notify("checkbox", "toggle")


# Client
mediator = Mediator()
checkbox = Checkbox(mediator)

checkbox.toggle()   
checkbox.toggle()   