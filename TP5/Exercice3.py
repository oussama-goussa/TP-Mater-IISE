if __name__ == "__main__":
    reponse = input("Voulez-vous ajouter des phrases au fichier 'phrases.txt' ? (oui/non) ").strip().lower()

    if reponse == "oui":

        while True:

            phrase = input("Entrez une phrase (ou tapez 'fin' pour arrêter) : ")

            if phrase.lower() == 'fin':
                break
            
            try:
                with open("TP5/phrases.txt", "a") as file:
                    file.write(phrase + "\n")
                    print(f"La phrase a été enregistrée dans le fichier.")
            except Exception as e:
                print(f"Une erreur est survenue lors de l'écriture dans le fichier : {e}")

    else:
        print("Aucune phrase n'a été ajoutée.")