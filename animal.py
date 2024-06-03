class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
    def breath(self):
        pass
class Bird(Animal):
    def make_sound(self):
        print("chirp")
    def move(self):
        print("Phin saw a bird flying away")
    def breath(self):
        print("huuuu")
class Fish(Animal):
    def make_sound(self):
        print("click")
    def move(self):
        print("swim")
    def breath(self):
        print("mmmmh")
class Dog(Animal):
    def make_sound(self):
        print("bark")
    def move(self):
        print("The dog runs daily as exercise")
    def breath(self):
        print("fffff")
class Human(Animal):
    def make_sound(self):
        print("talk")
    def move(self):
        print("Ajema walks to see Phin")
    def breath(self):
        print(" she breathes like mmmmmmhuuuuu")