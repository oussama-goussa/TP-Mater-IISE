class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def se_presenter(self):
        return "Je suis {} {} agé {} ans.".format(self.nom, self.prenom, self.age)
    
    def ajouter_ami(self ,ami):
        self.amis.append(ami)

    def afficher_amis(self):
        if not self.amis:
            print(self.prenom,"n'a pas encore d'amis.")
        else:
            print("Les amis de",self.prenom,"sont: ")
            for ami in self.amis:
                print("-",ami.prenom,ami.nom)

personne1 = Personne("Ali","Mohibe",20)
personne2 = Personne("Salm","Alali",19)
personne3 = Personne("Sana","Monir",21)

personne1.ajouter_ami(personne2)

personne1.afficher_amis()
personne3.afficher_amis()