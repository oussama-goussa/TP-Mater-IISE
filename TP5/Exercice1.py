with open("TP5/exemple.txt", "r") as file:
        lignes = file.readlines()
        for numero, ligne in enumerate(lignes, start=1):
            print(f"Ligne {numero}: {ligne.strip()}")