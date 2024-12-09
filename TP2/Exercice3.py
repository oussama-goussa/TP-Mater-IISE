class CompteBancaire:
    def __init__(self,titulaire,solde):
        self.titulaire = titulaire
        self.solde = solde
    
    def deposer(self,montant):
        self.solde += montant
        print(montant,"Dhs est deposé")
    
    def retirer(self,montant):
        if self.solde < montant:
            print("Le solde n'est pas suffisant.")
        else:
            self.solde -= montant
            print(montant,"Dhs est retiré")

    def afficher_solde(self):
        return "Le solde actuel est: {} Dhs".format(self.solde)
    
comp1 = CompteBancaire("Ali", 20000)

comp1.deposer(6000)
print(comp1.afficher_solde())

comp1.retirer(1200)
print(comp1.afficher_solde())