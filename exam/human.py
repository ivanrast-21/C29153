from person import Human
import random
human = Human(name='Антон', money = 46, mud = 100, health = 93)

human2 = Human(name='Кирил', money = 23, mud = 100, health = 86)

human3 = Human(name='Денис', money = 75, mud = 45, health = 73)

while True:
    a = 0
    print(human)
    print(human2)
    print(human3)
    i = random.randint(1, 2)
    if i == 1:
        try:
            human.chenge_stats(
                money = random.randint(20, 50),
                mud = random.randint(-25, -10),
                health = random.randint(-20, -10)
            )
        except:
          a += 1
        try:
            human2.chenge_stats(
                money=random.randint(20, 50),
                mud=random.randint(-25, -10),
                health=random.randint(-20, -10)
            )
        except:
            a+=1
        try:
            human3.chenge_stats(
                money=random.randint(20, 50),
                mud=random.randint(-25, -10),
                health=random.randint(-20, -10)
            )
        except:
            a+=1
    else:
        try:
            human.chenge_stats(
                money=random.randint(-20, -10),
                mud=random.randint(15, 20),
                health=random.randint(10, 20)
            )
        except:
            a+=1
        try:
            human2.chenge_stats(
                money=random.randint(-20, -10),
                mud=random.randint(10, 15),
                health=random.randint(10, 20)
            )
        except:
            a+=1
        try:
            human3.chenge_stats(
                money=random.randint(-20, -10),
                mud=random.randint(10, 15),
                health=random.randint(10, 20)
            )
        except:
            a += 1
        if a > 2:
            raise Exception('конец')
            break





