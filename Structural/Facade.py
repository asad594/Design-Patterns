#Facade design pattern aik structural design pattern hai jo 
# complex subsystem ko simplify karne ke liye ek unified 
# interface provide karta hai. Ye pattern client ko subsystem 
# ke multiple classes ke sath interact karne ki zarurat nahi 
# hoti, balki ek single interface ke through kaam ho jata hai.

#Facade pattern ka core idea: complex system ke aage ek simple, 
# single interface rakhna, taake client ko andar ke complicated 
# subsystems se direct deal na karna pare.        

class DVDPlayer:
    def on(self):
        print("DVD Player ON")
    def play(self):
        print("Playing movie")

class Projector:
    def on(self):
        print("Projector ON")
    def set_input(self):
        print("Projector input set to DVD")

class SoundSystem:
    def on(self):
        print("Sound System ON")
    def set_volume(self, level):
        print(f"Volume set to {level}")


class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.sound = SoundSystem()

    def watch_movie(self):
        print("--- Movie Mode Starting ---")
        self.dvd.on()
        self.projector.on()
        self.projector.set_input()
        self.sound.on()
        self.sound.set_volume(20)
        self.dvd.play()


home_theater = HomeTheaterFacade()
home_theater.watch_movie()