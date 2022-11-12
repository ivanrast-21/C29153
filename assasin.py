from cha import Cha
import random

class Assasin(Cha):
    def __init__(self, name='', health=1000, damage=1,defens=0):
        Cha.__init__(self, name, health, damage, defens )
        self.max = self.health
    def attack(self, target):
        a = random.randint(1, 100)
        if a <= 30:
            target.take_dam(1000)
        else:
            target.take_dam(self.damage)