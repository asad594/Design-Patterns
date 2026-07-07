#proxy aik structural design pattern hai jo aik object ka 
# surrogate ya placeholder provide karta hai. 
# Ye pattern client ko original object ke sath interact karne 
# ki ijazat deta hai, lekin proxy object ke through, 
# jo additional functionality ya control provide kar sakta hai.


#kisi object tak seedha access dene ke bajaye, uske aage ek 
# "middleman/substitute" rakho jo control kare ke access kab,
#  kaise, aur kise milega.

from abc import ABC, abstractmethod

# Common interface
class Internet(ABC):
    @abstractmethod
    def connect(self, site):
        pass

# Real Object
class RealInternet(Internet):
    def connect(self, site):
        print(f"Connecting to {site}")

# Proxy - middleman jo access control karta hai
class ProxyInternet(Internet):
    banned_sites = ["facebook.com", "youtube.com"]

    def __init__(self):
        self.real_internet = RealInternet()

    def connect(self, site):
        if site in self.banned_sites:
            print(f"Access Denied to {site}")
        else:
            self.real_internet.connect(site)   # asli kaam real object karega


# Client
internet = ProxyInternet()
internet.connect("google.com")
internet.connect("facebook.com")