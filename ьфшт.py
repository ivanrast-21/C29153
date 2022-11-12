from cha import Cha
from berserk import Berserk
from assasin import Assasin

import cha




player = Berserk(name='Din', damage = 10)
player2 = Cha(name='Dane', damage = 15)
player3 = Assasin(name='Sames', damage = 30)
print(player)
print(player2)
print(player3)
while True:
    player.attack(player2)
    player.attack(player3)
    player2.attack(player)
    player2.attack(player3)
    player3.attack(player2)
    player3.attack(player)


    print(player)
    print(player2)
    print(player3)


    if player.is_alive() == False:
        break
    elif player2.is_alive() == False:
        break
    elif player3.is_alive() == False:
        break




