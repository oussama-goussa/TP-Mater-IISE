class Voiture:
    def __init__(self,marque,modèle,année):
        self.marque = marque
        self.modèle = modèle
        self.année = année

    def afficher_info(self):
        return "La marque: {}, Le modèle: {}, l'année: {}".format(self.marque,self.modèle,self.année)
    
v1 = Voiture("Toyota","Corolla",2020)
v2 = Voiture("Ford","Mustang",2022)
v3 = Voiture("Tesla","Model S",2023)
v4 = Voiture("Honda","Civic",2018)

print(v1.afficher_info())
print(v2.afficher_info())
print(v3.afficher_info())
print(v4.afficher_info())