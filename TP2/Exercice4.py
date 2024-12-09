class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        return "Je suis {} {} agé {} ans.".format(self.nom, self.prenom, self.age)

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
    
    def etudier(self):
        return "{} {}, étudiant(e) (matricule : {}), est en train d'étudier.".format(self.nom, self.prenom, self.matricule)

personne1 = Personne("Ali", "Barada", 20)
print(personne1.se_presenter())

etudiant1 = Etudiant("GOUSSA","Oussama",21 ,2024001)
print(etudiant1.etudier())