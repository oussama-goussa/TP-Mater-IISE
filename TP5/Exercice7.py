import shutil
import os

journal = "TP5/journal.txt"
journal_copie = "TP5/journal_copie.txt"
deplacer  = "TP5/archives"

def creer_journal():

  with open(journal, "w") as fichier:
    fichier.write("Aujourd'hui, j'ai appris à programmer en Python.\n")
    fichier.write("C'est vraiment intéressant !\n")
    fichier.write("Demain, je vais essayer de créer un jeu simple.")

if __name__ == "__main__":
    creer_journal()

    try:
        shutil.copy(journal,journal_copie)
        print(f"Ficher copié de {journal} à {journal_copie}")
    except FileNotFoundError:
        print("Le fichier à source n'a pas été trouvé")
    except IOError:
        print("Erreur lors de la copie du fichier.")

    try:
        os.makedirs(deplacer, exist_ok=True)
        shutil.move(journal_copie,deplacer)
        print(f"Ficher déplacé de {journal_copie} à {deplacer}")
    except FileNotFoundError:
        print("Le fichier à déplacer n'a pas été trouvé")
    except IOError:
        print("Erreur lors de la déplacement du fichier.")