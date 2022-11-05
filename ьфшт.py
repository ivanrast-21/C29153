from cha import Cha
from berserk import Berserk

import cha




player = Berserk(name='Din', damage = 10)
player2 = Cha(name='Dane', damage = 15)
print(player)
print(player2)
while True:
    player.attack(player2)
    player2.attack(player)

    print(player)
    print(player2)
    print(player.c_a_d())

    if player.is_alive() == False:
        break
    elif player2.is_alive() == False:
        break




