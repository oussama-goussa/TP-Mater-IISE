import csv

contacts = [
    ["Nom", "Âge", "Ville"], 
    ["Alice", 30, "Paris"],
    ["Bob", 25, "Lyon"]
]

try:
    with open("TP5/contacts.csv", mode="w", newline="", encoding="utf-8") as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerows(contacts) 
    print(f"Le fichier a été créé avec succès et les informations ont été enregistrées.")
except Exception as e:
    print(f"Une erreur est survenue lors de la création du fichier : {e}")


try:
    with open("TP5/contacts.csv", newline='', encoding="utf-8") as fichiercsv:
        reader = csv.DictReader(fichiercsv)  
        for row in reader:
            print(f"Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")
except Exception as e:
    print(f"Une erreur est survenue lors de la lecture du fichier : {e}")
