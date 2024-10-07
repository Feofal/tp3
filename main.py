"""
    Nom: Gabriel Foriel Fusier
    Groupe: 401
    Description: Combat de monstre avec des dés
"""
import random
def dice(nb_dice,nb_face):
    total = 0
    for i in range(nb_dice):
        launch = random.randint( , nb_face)
        total += launch
    return total
def game():
    playing = True
    player_hp = 20
    number_enemy = 0
    number_fight = 0
    number_victory = 0
    number_defeated = 0
    consecutive_victory = 0
    while playing:
        if player_hp <= 0:
            playing = False
        if consecutive_victory % 3 == 0 and consecutive_victory != 0:
            enemy_type = "boss"
        else:
            enemy_type = "classic"
        number_enemy += 1
        enemy_strenght = dice(2,5)
        print(f"Vous tombez face à face avec un adversaire de difficulté {enemy_strenght}")
        action = int(input(("Que voulez-vous faire ?\n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie\n> ")))

        match action:
            case 1:
                if enemy_type == "boss":
                    enemy_life = 2
                    print("Oh non, devant vous ce trouve un boss")
                    double_life_enemy_message = "\nVous l'avez battu, mais, oh non, il se relève"
                else:
                    enemy_life = 1
                    double_life_enemy_message = ""
                for i in range(enemy_life):
                    number_fight += 1
                    attack = dice(2,6)
                    print(f"\nAdversaire : {number_enemy}\nForce de l’adversaire : {enemy_strenght}\nNiveau de vie de l’usager : {player_hp}\nCombat {number_fight} : {number_victory} vs {number_defeated}")
                    print(f"\nLancer du dé : {attack}")
                    if attack > enemy_strenght:
                        fight_status = "Victoire"
                        number_victory += 1
                        consecutive_victory += 1
                        player_hp += enemy_strenght
                        if i == 1:
                            double_life_enemy_message = ""
                        print(double_life_enemy_message)
                    else:
                        fight_status = "Défaite"
                        number_defeated += 1
                        consecutive_victory = 0
                        player_hp -= enemy_strenght
                        break

                print(f"Dernier combat = {fight_status}")
                if fight_status == "Victoire":
                    print(f"Niveau de vie : {player_hp} \nNombre de victoires consécutives : {consecutive_victory}")

            case 2:
                player_hp -= 1
                print(f"Vous avez perdu 1 pv\nIl vous reste {player_hp} pv")
            case 3:
                print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n")
            case 4:
                print("Merci et au revoir... ")
                playing = False
        print("___________________________________________________________")
    print(f"La partie est terminée, vous avez vaincu {number_victory} monstre(s).\n\n")

game()
