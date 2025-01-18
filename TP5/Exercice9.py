if __name__ == "__main__":
    try:
        with open("TP5/fichier.txt", "r") as fichier:
            contenu = fichier.readlines()

        nombre_lignes = 0
        nombre_mots = 0
        nombre_caracteres = 0

        for ligne in contenu:
            nombre_lignes += 1
            nombre_mots += len(ligne.split())
            nombre_caracteres += len(ligne)

        print(f"Les statistiques pour le fichier:")
        print(f" - Nombre total de lignes : {nombre_lignes}")
        print(f" - Nombre total de mots : {nombre_mots}")
        print(f" - Nombre total de caractères : {nombre_caracteres}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier n'existe pas.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
