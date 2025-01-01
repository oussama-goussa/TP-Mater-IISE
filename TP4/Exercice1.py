class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}")

class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print(f"Puissance : {self.puissance} chevaux, Type de moteur : {self.type_moteur}")

class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Nombre de places : {self.nombre_de_places}")

class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Type de moto : {self.type_moto}")

# La création d'une instance de Voiture
voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, puissance=150, type_moteur="Essence", nombre_de_places=5)

# La création d'une instance de Moto
moto = Moto(marque="Yamaha", modele="MT-07", annee=2021, puissance=74, type_moteur="Essence", type_moto="Sport")

# L'affichage des informations de la voiture
print("Les informations sur la voiture :")
voiture.afficher_info()

# L'affichage des informations de la moto
print("\nLes informations sur la moto :")
moto.afficher_info()

print(Voiture.mro())
