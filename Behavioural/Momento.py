# Momento aik design pattern ha jo aik object ka state ko 
# capture kar k store kar k rakhta ha taake future may us state
# ko restore kiya ja sakay.

#  Ye pattern aik object ka state ko encapsulate karta ha aur 
# usay aik separate object (momento) may store karta ha, 
# jisse original object ka state future may restore kiya ja 
# sakay. 

#Like the health in a game when we start the game the health
# of the player is 100% and when the player dies we can restore
# the health to 100% by using the momento pattern.

class Memento:
    def __init__(self, health):
        self.health = health

class GameCharacter:
    def __init__(self):
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        print("Health is now:", self.health)

    def save(self):
        return Memento(self.health)

    def restore(self, memento):
        self.health = memento.health
        print("Restored health to:", self.health)


character = GameCharacter()

save_point = character.save()  
character.take_damage(30)   
character.take_damage(40)  

character.restore(save_point)   