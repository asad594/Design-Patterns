# FLyweight aik structural design pattern hai jo memory ko
#  optimize karne ke liye use hota hai. Ye pattern shared
#  objects ka use karta hai jahan multiple objects same data ko
#  share karte hain, taake memory ka efficient use ho sake.

class BulletType:
    def __init__(self, color):
        self.color = color   # shared/common data
    def show(self, x, y):
        print(f"{self.color} bullet fired at ({x}, {y})")

# Factory - ek hi type dobara nahi banayega
bullet_types = {}
def get_bullet_type(color):
    if color not in bullet_types:
        print("Creating new bullet type:", color)
        bullet_types[color] = BulletType(color)
    return bullet_types[color]

# Client
red = get_bullet_type("Red")
red.show(10, 20)
red.show(15, 30)   # same object reuse hua, dobara nahi bana

blue = get_bullet_type("Blue")
blue.show(50, 60)