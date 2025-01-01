import csv
import os

nom_fichier = "TP5/contacts.csv"

# Vérifier si le fichier existe, sinon le créer avec des en-têtes
if not os.path.exists(nom_fichier):
    with open(nom_fichier, mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "Âge", "Ville"])  # En-têtes

def ajouter_contact(nom_fichier):
    with open(nom_fichier, 'a', newline='', encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        nom = input("Entrez le nom : ")
        age = input("Entrez l'âge : ")
        ville = input("Entrez la ville : ")
        writer.writerow([nom, age, ville])
        print("Contact ajouté avec succès !")

def afficher_contacts(nom_fichier):
    with open(nom_fichier, 'r', encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)
        print("\nListe des contacts :")
        for row in reader:
            print(f"Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")

def rechercher_contact(nom_fichier, nom_a_chercher):
    with open(nom_fichier, 'r', encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)
        for row in reader:
            if row["Nom"].lower() == nom_a_chercher.lower():
                print(f"Contact trouvé : Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")
                return
        print("Contact non trouvé.")

def supprimer_contact(nom_fichier, nom_a_supprimer):
    lignes = []
    with open(nom_fichier, 'r', encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)
        en_tetes = reader.fieldnames
        for row in reader:
            if row["Nom"].lower() != nom_a_supprimer.lower():
                lignes.append(row)

    with open(nom_fichier, 'w', newline='', encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=en_tetes)
        writer.writeheader()  # Réécrire les en-têtes
        writer.writerows(lignes)
    print("Contact supprimé avec succès !")

if __name__ == "__main__":
    while True:
        print("\nMenu :")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choix = input("Choisissez une option (1-5) : ")

        if choix == '1':
            ajouter_contact(nom_fichier)
        elif choix == '2':
            afficher_contacts(nom_fichier)
        elif choix == '3':
            nom_a_chercher = input("Entrez le nom à chercher : ")
            rechercher_contact(nom_fichier, nom_a_chercher)
        elif choix == '4':
            nom_a_supprimer = input("Entrez le nom à supprimer : ")
            supprimer_contact(nom_fichier, nom_a_supprimer)
        elif choix == '5':
            break
        else:
            print("Choix invalide.")
