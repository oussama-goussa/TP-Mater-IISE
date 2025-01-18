if __name__ == "__main__":
    try:
        with open("TP5/inexistant.txt", "r") as fichier:
            contenu = fichier.read()
            print("Contenu du fichier :")
            print(contenu)
    except FileNotFoundError:
        print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
