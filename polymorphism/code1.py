#Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling make_sound().

class Animal:
    def make_sound(self):
        print("Animal makes sounds")
class Dog(Animal):
    def make_sound(self):
        print("Bow bow")
class Cat(Animal):
    def make_sound(self):
        print("MewMew")
class Cow(Animal):
    def make_sound(self):
        print("MoohMooh")
l=[Animal(),Dog(),Cat(),Cow()]
for i in l:
    i.make_sound()
