from cha import Cha
import cha




player = Cha(name='Din', damage = 10)
player2 = Cha(name='Dane', damage = 7)
print(player)
print(player2)
while True:
    player.attack(player2)
    player2.attack(player)

    print(player)
    print(player2)

    if player.is_alive() == False:
        break
    elif player2.is_alive() == False:
        break




