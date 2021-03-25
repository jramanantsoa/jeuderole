import random

player = 50
ennemy = 50
potions = 3
menu =["1","2"]

while player > 0 and ennemy > 0:
    choice =input(" 1 Attack or 2  use potion ? ")
    if choice == "2":
        if potions == 0:
            print("No more potions")
        else:
            player = player+random.randint(15,50)
            potions = potions-1
            print(f"HP after potion {player}")
            #the ennemy attacks twice
            player = player - random.randint(5,15)
            #print(f"ennemy first attack :{player}")
            player = player - random.randint(5,15)
            #print(f"ennemy second attack :{player}")
    if choice == "1":
        ennemy = ennemy - random.randint(5,10)
        player = player - random.randint(5,15)
    print(f"PLayer : {player} / Ennemy : {ennemy}")
    print(potions)
    if player <=0:
        print("You lost the game.")
        break
    if ennemy <=0:
        print("You won the game.")
        break