import random
class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    
    def attack(self, other, weapon, atk):
        print(f"{self.name} hit {other.name} with a(n) {self.weapon} for {self.atk} damage")
        other.hp -= self.atk
        print(f"{other.name} has {other.hp}hp left")

    def isAlive(self):
        if self.hp > 0:
            return True
        return False
    
class Hero(Character):
    def __init__(self, name, hp, atk, weapon, specialMove, specialMoveDamage):
        super().__init__(name, hp, atk)
        self.weapon = weapon
        self.specialMove = specialMove
        self.specialMoveDamage = specialMoveDamage
    
    def superMove(self, other):
        print(f"{self.name} uses his special move {self.specialMove} for {self.specialMoveDamage} damage")
        other.hp -= self.specialMoveDamage
        print(f"{other.name} has {other.hp}hp left")


class Villain(Character):
    def __init__(self, name, hp, atk, weapon):
        super().__init__(name, hp, atk)
        self.weapon = weapon
    
    def superMove(self, other):
        print(f"{self.name} summons his minons")
        other.hp -= (self.atk + 40)
        print(f"{other.name} has {other.hp}hp left")


def battle(char1, char2):
    while char1.isAlive() and char2.isAlive():
        dice = random.randint(1, 7)
        if dice % 2 == 0:
            char1.attack(char2, char1.weapon, char1.atk)
        else:
            char2.attack(char1, char2.weapon, char2.atk)
        
        if dice % 3 == 0:
            char1.superMove(char2)
        if dice % 5 == 0:
            char2.superMove(char1)
    if char1.isAlive():
        print(f"{char1.name} Wins!!!")
    else:
        print(f"{char2.name} Wins!!")

hero = Hero("Temur", 500, 50, "Scythe", "TwinDragonBlast", 60)
villian = Villain("Mahmood", 500, 40, "Sword")

battle(hero, villian)