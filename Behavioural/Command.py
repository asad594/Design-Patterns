# Command pattern aik behavioral design pattern hai jis may hum 
# request ko aik object may encapusalte kartay ha that contains
# all information of the request. Ye pattern allow karta hai 
# ke hum request ko parameterize kar saken, queue kar saken,
#  log kar saken, or undo/redo functionality

from abc import ABC, abstractmethod

class Light:
    def on(self):
        print("Light is ON")
    def off(self):
        print("Light is OFF")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.off()
    def undo(self):
        self.light.on()

class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command):
        command.execute()
        self.history.append(command)   # undo ke liye store

    def press_undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()


light = Light()
on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

remote = RemoteControl()

remote.press_button(on_command)   
remote.press_button(off_command)   
remote.press_undo()                