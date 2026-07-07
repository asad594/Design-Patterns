# State ek behavioral design pattern hai jo kisi object ko uski 
# internal state change hone par apna behavior change karne 
# deta hai — is tarah ke lagta hai jaise object ne apni class
# hi badal li ho. Har state ko ek alag class mein represent kiya
# jata hai, aur object apna behavior us state ke hisab se 
# runtime pe dynamically switch karta hai, bina lambi 
# if-else/switch conditions likhe.


from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, light):
        pass

# Concrete States
class RedState(State):
    def handle(self, light):
        print("Red -> Stop")
        light.set_state(GreenState())

class GreenState(State):
    def handle(self, light):
        print("Green -> Go")
        light.set_state(YellowState())

class YellowState(State):
    def handle(self, light):
        print("Yellow -> Slow down")
        light.set_state(RedState())

class TrafficLight:
    def __init__(self):
        self.state = RedState()   # initial state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


light = TrafficLight()
light.request()   # Red -> Stop
light.request()   # Green -> Go
light.request()   # Yellow -> Slow down
light.request()   # Red -> Stop (cycle repeat)