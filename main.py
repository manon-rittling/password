# importe les bibliothèques nécessaires pour le programme 
import hashlib
import json
import random
import string

# Fonction pour générer un mot de passe aléatoire
def mdp_aleatoire():

    # liste des caractères autorisés pour le mot de passe aléatoire (lettres majuscules et minuscules, chiffres et caractères spéciaux)
    liste_charac = string.ascii_letters + string.digits + string.punctuation 
    mdp=""
    for index in range(15): # boucle pour générer un mot de passe de 10 caractères
        mdp += random.choice(liste_charac) # ajouter un caractère aléatoire à la chaîne de caractères mdp à chaque itération de la boucle for

    # hasher le mot de passe
    h_mdp = hashlib.sha256(mdp.encode()).hexdigest()

    # ajouter le mot de passe à la liste
    mdp_list.append(h_mdp)

    # enregistrer la liste mise à jour dans le fichier mdp.json 
    with open("mdp.json", "w") as fichier: # ouvrir le fichier mdp.json en mode écriture 
        json.dump(mdp_list, fichier, indent=2) # enregistrer la liste dans le fichier mdp.json, indent=2 pour un affichage plus lisible indente mon texte dans ma liste  
        fichier.write("\n") 
     
    print("Votre mot de passe aléatoire est : " + mdp)
    print("Le mot de passe hashé est : " + h_mdp)

# Fonction pour vérifier si le mot de passe est valide
def verif_mdp(mdp):
    while True:
        # Vérification de la longueur minimale du mot de passe (au moins 8 caractères)
        if len(mdp) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères")

        # Vérification de la présence d'au moins une lettre majuscule
        if not any(char.isupper() for char in mdp): #si aucune majuscule n'est trouvé dans le mot de passe, la condition sera True, et le bloc elif sera exécuté, affichant le message indiquant que le mot de passe doit contenir au moins un caractère spécial
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
                with open("mdp.json", "r") as fichier: #
                    try:
                        liste_h_mdp = json.load(fichier)
                    except json.decoder.JSONDecodeError: # si le fichier est vide, la liste est vide 
                        liste_h_mdp = [] # créer une liste vide
            except FileNotFoundError: # si le fichier n'existe pas, la liste est vide
                liste_h_mdp = [] # créer une liste vide

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

            return True

        # Demander à l'utilisateur de saisir un nouveau mot de passe
        mdp = input("Veuillez saisir un nouveau mot de passe : ")

# fonction pour ajouter un mot de passe à la liste des mots de passe dans le fichier JSON
def ajouter_mdp(mdp_list, nouveau_mdp_hash):
    # Vérifier si le mot de passe est déjà présent dans la liste
    if nouveau_mdp_hash in mdp_list: 
        print("Le mot de passe est déjà présent dans la liste.")
        return False
    else:
        # Ajouter le mot de passe à la liste et enregistrer la liste mise à jour dans le fichier mdp.json
        mdp_list.append(nouveau_mdp_hash)
        print("Le mot de passe a été ajouté à la liste du fichier mdp.json.")
        return True

# fonction pour afficher la liste des mots de passe dans le fichier JSON 
def afficher_mdp(mdp_list): 
    print("Liste des mots de passe enregistrés :")
    for mdp in mdp_list: # boucle pour afficher chaque mot de passe de la liste
        print(mdp) # afficher le mot de passe

# Charger la liste des mots de passe depuis le fichier JSON
try: # essayer d'ouvrir le fichier mdp.json
    with open("mdp.json", "r") as fichier: # ouvrir le fichier mdp.json en mode lecture seule 
        mdp_list = json.load(fichier) # charger le contenu du fichier dans la variable mdp_list 
except FileNotFoundError: # si le fichier n'existe pas, la liste est vide 
    mdp_list = [] # créer une liste vide

# boucle while pour afficher le menu
while True:
    try:
        # Afficher le menu
        choix_menu = input("Choisissez une option :\n1. Ajouter un nouveau mot de passe\n2. Afficher mes mots de passe\n3. mot de passe aleatoire\n4. Quitter\n")

        if choix_menu == "1": #en appuyant sur 1, on ajoute un mot de passe
            # Appeler la fonction pour ajouter un mot de passe
            choix_mdp = input("Veuillez saisir votre mot de passe\n avec minimum 8 caracteres\n minimum une majuscule\n minimum une minuscule\n minimum un chiffre et un caractere special : ")

            verif_mdp(choix_mdp)
            ajouter_mdp(mdp_list, hashlib.sha256(choix_mdp.encode()).hexdigest())

        elif choix_menu == "2":
            #appler la fonction pour afficher les mots de passe
            afficher_mdp(mdp_list)
        elif choix_menu == "3":
            # Appeler la fonction pour afficher un mot de passe aléatoire
            mdp_aleatoire()

        elif choix_menu == "4":
            # Appeler la fonction pour quitter
            print("Merci d'avoir utilisé notre programme.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
    except KeyboardInterrupt: # si l'utilisateur appuie sur Ctrl+C, le programme s'arrête 
        print("\nInterruption utilisateur. Programme arrêté.")
        break
