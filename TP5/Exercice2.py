if __name__ == "__main__":
    phrase1 = input("Entrez la première phrase: ")
    phrase2 = input("Entrez la deuxième phrase: ")
    phrase3 = input("Entrez la troisième phrase: ")

    try:
        with open("TP5/phrases.txt", "w") as file:
            file.write(phrase1 + "\n")
            file.write(phrase2 + "\n")
            file.write(phrase3 + "\n")
        print(f"Les phrases ont été enregistrées dans le fichier.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'écriture dans le fichier : {e}")
