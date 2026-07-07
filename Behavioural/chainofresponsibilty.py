#behavioural design patterns woh design patterns hain jo 
# objects ke beech communication aur responsibility ko manage
#  karte hain. Ye patterns ye ensure karte hain ke objects ka
#  interaction flexible aur maintainable ho, taake complex
#  systems mein changes ko easily implement kiya ja sake.

#chainofresponsibility pattern aik behavioural design pattern 
# hai jo allow karta hai ke multiple objects ek request ko 
# handle karen agr koi reuqest ati ha to woh kesay handle ho gi 
#phelay handler A ko pass ho gi agr woh nhi handle kar sakta to
# woh handler B ko pass ho gi aur aise hi kam karay gi jab tak
# koi handler request ko handle na kar le ya chain khatam na ho jaye.

#har handler apna kam karta hai aur agr woh request ko handle
# nahi kar sakta to woh dosray handler ko pass kar deta ha jab 
# tak chain khatam na ho jaii

#like agr Office mein leave application socho. Pehle Team Lead 
# ke paas jati hai — agar 2 din ki leave hai to wo khud approve
# kar deta hai. Agar zyada din ki hai to wo Manager ko forward 
# karta hai. Manager na kar sake to HR/Director ko forward hota 
# hai. Tumhe pata nahi kaun approve karega — request khud chain 
# mein aage badhti jaati hai.

#-------------------- Code Example --------------------
from abc import ABC, abstractmethod

class Approver(ABC):
    def __init__(self):
        self.next_approver = None

    def set_next(self, approver):
        self.next_approver = approver

    @abstractmethod
    def handle(self, days):
        pass

class TeamLead(Approver):
    def handle(self, days):
        if days <= 2:
            print(f"TeamLead approved {days} day(s) leave")
        elif self.next_approver:
            self.next_approver.handle(days)

class Manager(Approver):
    def handle(self, days):
        if days <= 5:
            print(f"Manager approved {days} day(s) leave")
        elif self.next_approver:
            self.next_approver.handle(days)

class Director(Approver):
    def handle(self, days):
        print(f"Director approved {days} day(s) leave")


# Chain banao
team_lead = TeamLead()
manager = Manager()
director = Director()

team_lead.set_next(manager)
manager.set_next(director)

# Client - sirf pehle handler ko call karta hai
team_lead.handle(1)    # TeamLead approved
team_lead.handle(4)    # Manager approved
team_lead.handle(10)   # Director approved