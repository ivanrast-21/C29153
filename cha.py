
class Cha:
    name =''
    health = 300
    damage =1
    defens = 0
    def __init__(self, name='', health = 300, damage=1, defens=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defens = defens
    def __str__(self):
        return f' == {self.name} ==\n' \
               f' health = {self.health}\n' \
               f' damage = {self.damage}\n' \
               f' defens = {self.defens}\n'
    def take_dam(self, damage=0):
        self.health -= max(damage, 0)
    def attack(self, target):
        target.take_dam(self.damage)
    def is_alive(self):
        if self.health == 0:
            return False
        elif self.health < 0:
            return False
        else:
            return True


