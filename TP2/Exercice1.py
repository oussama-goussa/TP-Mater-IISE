class Chien:
    def __init__(self,nom,race,age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        return "Woof!"
    
ch1 = Chien("Lopi", "Chihuahua", 2)
print(ch1.aboyer())