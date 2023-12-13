# importation des modules nécessaires au fonctionnement du programme   
import hashlib
import json
import random
import string

# Fonction pour vérifier si le mot de passe est valide
def verif_mdp(mdp):
    while True:
        # Vérification de la longueur minimale du mot de passe (au moins 8 caractères)
        if len(mdp) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères")

        # Vérification de la présence d'au moins une lettre majuscule
        if not any(char.isupper() for char in mdp):
            print("Le mot de passe doit contenir au moins une lettre majuscule")

        # Vérification de la présence d'au moins une lettre minuscule
        if not any(char.islower() for char in mdp):
            print("Le mot de passe doit contenir au moins une lettre minuscule")

        # Vérification de la présence d'au moins un chiffre
        if not any(char.isdigit() for char in mdp):
            print("Le mot de passe doit contenir au moins un chiffre")

        # Vérification de la présence d'au moins un caractère spécial
        if not any(char in "!@#$%^&*()-+?_=,<>/" for char in mdp):
            print("Le mot de passe doit contenir au moins un caractère spécial")

        # Si toutes les conditions de sécurité sont remplies, le mot de passe est considéré comme valide
        else:
            # hasher le mot de passe
            h_mdp = hashlib.sha256(mdp.encode()).hexdigest()
            
            # Lire le fichier JSON existant s'il existe
            try:
                with open("mdp.json", "r") as fichier:
                    try:
                        liste_h_mdp = json.load(fichier)
                    except json.decoder.JSONDecodeError:
                        liste_h_mdp = []
            except FileNotFoundError:
                liste_h_mdp = []
                
                with open("mdp.json", "w") as fichier:
                    json.dump(liste_h_mdp, fichier, indent=2)

            # Ajouter le nouveau mot de passe à la liste
            liste_h_mdp.append(h_mdp)
            
            # Enregistrer la liste mise à jour dans le fichier mdp.json
            with open("mdp.json", "w") as fichier:
                json.dump(liste_h_mdp, fichier, indent=2) 
                fichier.write("\n") 

            # message de confirmation
            print("Le mot de passe est valide")
            # Afficher le mot de passe hashé
            print("Le mot de passe hashé est : " + h_mdp)
            print("Le mot de passe a été enregistré dans le fichier mdp.json") 

            return True
        
        # Demander à l'utilisateur de saisir un nouveau mot de passe
        mdp = input("Veuillez saisir un nouveau mot de passe valide1 : ")


def ajouter_mdp(mdp_list, nouveau_mdp):
    # Vérifier si le mot de passe est déjà présent
    if nouveau_mdp in mdp_list:
        print("Ce mot de passe existe déjà. Veuillez en choisir un nouveau.")
        return False

    # Ajouter le nouveau mot de passe à la liste
    mdp_list.append(nouveau_mdp)
    return True

def afficher_mdp(mdp_list):
    print("Liste des mots de passe enregistrés :")
    for mdp in mdp_list:
        print(mdp)

# Charger la liste des mots de passe depuis le fichier JSON
try:
    with open("mdp.json", "r") as fichier:
        mdp_list = json.load(fichier)
except FileNotFoundError:
    mdp_list = []

# Demander à l'utilisateur de saisir un mot de passe
choix_mdp = input("Veuillez saisir votre mot de passe :\n")

# Appeler la fonction de vérification du mot de passe
if verif_mdp(choix_mdp):
    # Hacher le mot de passe
    h_mdp = hashlib.sha256(choix_mdp.encode()).hexdigest()
    
    # Ajouter le nouveau mot de passe à la liste (si valide)
    if ajouter_mdp(mdp_list, h_mdp):
        # Enregistrer la liste mise à jour dans le fichier mdp.json
        with open("mdp.json", "w") as fichier:
            json.dump(mdp_list, fichier, indent=2) 
            fichier.write("\n")

    # # Afficher la liste des mots de passe
    # afficher_mdp(mdp_list)

# boucle while pour afficher le menu
while True:
    try:
        # Afficher le menu
        choix_menu = input("Choisissez une option :\n1. Ajouter un nouveau mot de passe\n2. Afficher mes mots de passe\n3. Quitter\n")

        if choix_menu == "1":
            # Appeler la fonction pour ajouter un mot de passe
            choix_mdp = input("Veuillez saisir votre mot de passe\n avec minimum 8 caracteres\n minimum une majuscule\n minimum une minuscule\n minimum un chiffre et un caractere special : ")
            verif_mdp(choix_mdp)
        elif choix_menu == "2":
            #appler la fonction pour afficher les mots de passe
            afficher_mdp(mdp_list)
        elif choix_menu == "3":
            # Appeler la fonction pour quitter
            print("Merci d'avoir utilisé notre programme.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
    except KeyboardInterrupt:
        print("\nInterruption utilisateur. Programme arrêté.")
        break


verif_mdp(choix_mdp)
