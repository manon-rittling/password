import hashlib
import json


# Fonction pour vérifier si le mot de passe est valide
def verif_mdp(mdp):
    while True:
        
        # Vérification de la présence d'au moins 8 caractères
        if len(mdp) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères")

        # Vérification de la présence d'au moins une lettre majuscule
        elif not any(char.isupper() for char in mdp): # not any() renvoie True si aucun caractère n'est majuscule dans le mot de passe, isupper() renvoie True si le caractère est majuscule
            print("Le mot de passe doit contenir au moins une lettre majuscule")

        # Vérification de la présence d'au moins une lettre minuscule
        elif not any(char.islower() for char in mdp):
            print("Le mot de passe doit contenir au moins une lettre minuscule")

        # Vérification de la présence d'au moins un chiffre
        elif not any(char.isdigit() for char in mdp):
            print("Le mot de passe doit contenir au moins un chiffre")

        # Vérification de la présence d'au moins un caractère spécial
            
        elif not any(char in "!@#$%^&*()-+?_=,<>/"   for char in mdp): # not any() renvoie True si aucun caractère spécial n'est présent dans le mot de passe
            print("Le mot de passe doit contenir au moins un caractère spécial")

        # Si toutes les conditions sont remplies, le mot de passe est valide
        else:
            # hasher le mot de passe
            h_mdp = hashlib.sha256(choix_mdp.encode()).hexdigest() # encode() convertit le mot de passe en bytes, hexdigest() convertit le hash en hexadécimal
             
            with open("mdp.json", "a") as fichier:
                json.dump(h_mdp, fichier)
                fichier.write("\n")
                
            
            # message de confirmation
            print("Le mot de passe est valide")

            # Afficher le mot de passe hashé
            print("Le mot de passe hashé est : " + h_mdp)

            print("Le mot de passe a été enregistré dans le fichier mdp.json") 
            
            return True
        
        # Demander à l'utilisateur de saisir un nouveau mot de passe
        mdp = input("Veuillez saisir un nouveau mot de passe : ")
        

# Demander à l'utilisateur de saisir un mot de passe
choix_mdp = input("Veuillez saisir votre mot de passe : ")

# Appeler la fonction de vérification du mot de passe
verif_mdp(choix_mdp)





