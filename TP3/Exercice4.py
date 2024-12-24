class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.set_prix(prix)  # Utilisation de set_prix pour valider le prix

    def getNom(self):
        return self.__nom
    
    def getPrix(self):
        return self.__prix
    
    def set_prix(self, prix):
        if isinstance(prix, (int, float)) and prix >= 0:
            self.__prix = prix
        else:
            raise ValueError("Le prix doit être un nombre positif.")
        
    def calculer_prix_remise(self, remise, seuil):
        if self.__prix > seuil:
            prix_remise = self.__prix * (1 - remise / 100)
            return prix_remise
        return self.__prix
    
if __name__ == "__main__":
    try:
        produit1 = Produit("Ordinateur", 3500)  # Prix valide

        remise = 10 
        seuil = 2500

        print(f"Produit : {produit1.getNom()}, Prix sans remise : {produit1.getPrix()} Dhs, Prix avec remise : {produit1.calculer_prix_remise(remise, seuil):.2f} Dhs")
    except ValueError as e:
        print(e)
