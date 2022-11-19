from Action import A1ction
from Work import Work
from Rest import Rest
class Human:
    name = ''
    health = 100
    mud = 100
    money = 50
    def __init__(self, name, health, mud, money):
        self.name = name
        self.health = health
        self.mud = mud
        self.money = money
    def __str__(self):
        return \
            f'=== {self.name} ===\n' \
            f' Здоровье: {self.health}\n' \
            f' Настороение: {self.mud}\n' \
            f' Деньги: {self.money}\n'
    def do(self, action):
        self.money += action.money
        self.mud += action.mud
        self.health += action.health
        if self.mud < 0:
            raise Exception('Нет насторения')
        if self.health < 0:
            raise Exception('Нет здоровя')
        if action.health > 100:
            self.health = 15
        if action.mud > 100:
            self.mud = 15
        go_to_factory = Work(name='Пойти на завод', money=50, mud=-10, health=-3)
        go_to_park = Rest(name='Сходить в парк', money=0, mood=15, health=3)
        go_to_hospital = A1ction(name='Пойти в больницу', money=-20, mood=-5, health=20)


    def chenge_stats(self, money = 0, mud = 0, health = 0):
        self.money += money
        self.mud += mud
        self.health += health
        if self.mud < 0:
            raise Exception('Нет насторения')
        if self.health < 0:
            raise Exception('Нет здоровя')
        if health > 100:
            self.health = 15
        if mud > 100:
            self.mud = 15


