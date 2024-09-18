"""
    Nom: Gabriel Foriel Fusier
    Groupe: 401
    Description: Combat de monstre avec des dés
"""
import random
def dice(nb_dice,nb_face):
    total = 0
    for i in range(nb_dice):
        launch = random.randint(1, nb_face)
        total += launch
    return total
def game():
    player_hp = 20
    number_enemy = 0
    number_fight = 0
    number_victory = 0
    number_defeated = 0
    consecutive_victory = 0
    while True:
        if player_hp <= 0:
            break
        #1 = classic 2 = boss
        if consecutive_victory % 3 == 0:
            enemy_type = 1
        else:
            enemy_type = 2
        number_enemy += 1
        enemy_strenght = dice(1,5)
        print(f"Vous tombez face à face avec un adversaire de difficulté {enemy_strenght}")
        action = int(input(("Que voulez-vous faire ?\n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie\n> ")))

        match action:
            case 1:


                number_fight += 1
                attack = dice(1,6)
                print(f"\nAdversaire : {number_enemy}\nForce de l’adversaire : {enemy_strenght}\nNiveau de vie de l’usager : {player_hp}\nCombat {number_fight} : {number_victory} vs {number_defeated}")
                print(f"\nLancer du dé : {attack}")
                if attack > enemy_strenght:
                    fight_status = "Victoire"
                    number_victory += 1
                    consecutive_victory += 1
                    player_hp += enemy_strenght
                else:
                    fight_status = "Défaite"
                    number_defeated += 1
                    consecutive_victory = 0
                    player_hp -= enemy_strenght
                print(f"Dernier combat = {fight_status}")
                if fight_status == "Victoire":
                    print(f"Niveau de vie : {player_hp} \nNombre de victoires consécutives : {consecutive_victory}")

            case 2:
                player_hp -= 1
            case 3:
                print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n")
            case 4:
                print("Merci et au revoir... ")
                break
    print(f"La partie est terminée, vous avez vaincu {number_victory} monstre(s).")
game()