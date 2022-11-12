from cha import Cha

class Berserk(Cha):
    max = 1000
    def __init__(self, name='', health=1000, damage=1, defence=0):
        Cha.__init__(self, name, health, damage, defence)
        self.max = self.health
    def c_a_d(self):
        return self.damage * (1 - self.health / self.max)
    def attack(self, target):
        target.take_dam(self.damage + self.c_a_d())


