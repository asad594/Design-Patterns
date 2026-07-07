# Observer aik design patttern jis may aik object (subject) ka
# state change hota hai aur us state change ko notify karna hota
# hai dusre objects (observers) ko. Ye pattern loosely coupled 
# design provide karta hai jahan subject aur observers ke beech 
# direct dependency nahi hoti.

#Observer ek behavioral design pattern hai jisme ek object 
#(jise Subject kehte hain) ki state change hone par uske saare 
#dependent objects (jinhe Observers kehte hain) ko automatically
# notify kiya jata hai — bina Subject ko Observers ke internal 
# details (kaun hain, kitne hain, kya karte hain) jaanne ki 
# zaroorat ke. Ye one-to-many dependency define karta hai jahan 
# ek Subject ki state change hone par uske saare registered 
# Observers automatically update ho jate hain.

from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, video_title):
        pass

class User(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, video_title):
        print(f"{self.name} notified: New video '{video_title}' uploaded!")

class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def upload_video(self, title):
        print(f"\n{self.name} uploaded: {title}")
        self.notify_all(title)

    def notify_all(self, title):
        for sub in self.subscribers:
            sub.update(title)


channel = YouTubeChannel("CodeWithAsad")

ali = User("Ali")
sara = User("Sara")

channel.subscribe(ali)
channel.subscribe(sara)

channel.upload_video("Observer Pattern Explained")

channel.unsubscribe(sara)
channel.upload_video("Design Patterns Series")