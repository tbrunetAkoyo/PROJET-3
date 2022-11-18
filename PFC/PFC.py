import random

def game():
    nom = input("veuillez saisir votre nom : ")
    score_Player = 0
    score_IA = 0
    égalité = 0

    while True :
        print(nom," : ", score_Player," égalités : ", égalité, " PC : ", score_IA)
        coupJoueur = input("Entrez votre coup : Pierre, Feuille, Ciseaux :")
        if coupJoueur =="q" :
            print("Fin de la partie")
            break
        if coupJoueur != "p" and coupJoueur != "f" and coupJoueur != "c" :
            continue
            

        if coupJoueur == "p" :
            print("Pierre contre ", end=" ")
        elif coupJoueur == "f" :
            print("Feuille contre ", end=" ")
        else:
            print("Ciseaux contre ", end=" ")

        randomNombre = random.randint(1,3)
        if randomNombre == 1 :
            coupPC = "p"
            print("Pierre")
        elif randomNombre == 2 :
            coupPC = "f"
            print("Feuille")
        else :
            coupPC = "c"
            print("Ciseaux")

        if coupJoueur == coupPC :
            print("Match nul !")
            égalité = égalité + 1
        elif coupJoueur =="p" and coupPC =="c" :
            print("Vous avez gagné !")
            score_Player = score_Player + 1
        elif coupJoueur =="f" and coupPC =="p" :
            print("Vous avez gagné !")
            score_Player = score_Player + 1
        elif coupJoueur =="c" and coupPC =="f" :
            print("Vous avez gagné !")
            score_Player = score_Player + 1
        elif coupJoueur =="c" and coupPC =="p" :
            print("Vous avez perdu !")
            score_IA = score_IA + 1
        elif coupJoueur =="p" and coupPC =="f" :
            print("Vous avez perdu !")
            score_IA = score_IA + 1
        elif coupJoueur =="f" and coupPC =="c" :
            print("Vous avez perdu !")
            score_IA = score_IA + 1

        if score_IA == 5:
            print("Le score est de", score_Player, "a", score_IA, "avec", égalité, "égalités")
            print("DOMMAGE, vous gagnerez une prochaine fois")
            break
        elif score_Player == 5:
            print("Le score est de", score_Player, "a", score_IA, "avec", égalité, "égalités")
            print("BRAVO, vous avez gagnez")
            break