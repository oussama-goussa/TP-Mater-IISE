class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_montant(self):
        return self.produit.prix * self.quantite

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = 0
        for commande in self.commandes:
            total += commande.calculer_montant()
        return total

# Exemple d'utilisation
produit1 = Produit("Livre", 50)
produit2 = Produit("Cahier", 21)

commande1 = Commande(produit1, 3)
commande2 = Commande(produit2, 2)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

print("Total du panier :", panier.calculer_total(),"Dhs")