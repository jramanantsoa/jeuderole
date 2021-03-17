#initialisation du nombre de vie de mon player et de l'ennemi + nb de potions
moi = 50
ennemi = 50
choix_possibles =["1","2"]
#choix possibles
while moi > 0 and ennemi >0:
    choix  = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
    if choix not in choix_possibles:
        print("Entrer un choix valide")
#attaquer
#prendre une potion
#fin de partie
