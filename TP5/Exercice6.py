import os

ancien_nom = "T5/phrases.txt"
nouveau_nom = "T5/anciennes_phrases.txt"

try:
    os.rename(ancien_nom,nouveau_nom)
    print(f"Ficher renommé en {nouveau_nom}")
except FileNotFoundError:
    print("Le fichier à renommer n'a pas été trouvé")
except IOError:
    print("Erreur lors du renommage du fichier.")

try:
    os.remove(nouveau_nom)
    print(f"Ficher {nouveau_nom} supprimé.")
except FileNotFoundError:
    print("Le fichier à supprimer n'a pas été trouvé")
except IOError:
    print("Erreur lors de la suppression du fichier.")

