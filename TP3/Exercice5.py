class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_informations(self):
        return f"Nom : {self.nom}, Prénom : {self.prenom}, Salaire : {self.salaire:.2f} Dhs"

class Manager(Employe):
    def __init__(self, nom, prenom, salaire, employes=None):
        super().__init__(nom, prenom, salaire)
        self.employes_supervises = employes or []

    def ajouter_employe(self, employe):
        if isinstance(employe, Employe) and employe not in self.employes_supervises:
            self.employes_supervises.append(employe)
        else:
            print("L'objet ajouté doit être une instance d'Employe et ne pas déjà être supervisé.")

    def afficher_employes_supervises(self):
        if not self.employes_supervises:
            return "Aucun employé sous supervision"
        else:
            return "\nEmployés supervisés :\n" + "\n".join(
                f"- {employe.nom} {employe.prenom}" for employe in self.employes_supervises
            )
       
if __name__ == "__main__":

    employe1 = Employe("Omar", "Ali", 3800)
    employe2 = Employe("Oussa", "Omar", 4200)
    employe3 = Employe("Ouchen", "Sana", 2400)

    employes_supervises = [employe1,employe2]

    manager1 = Manager("EL-Maride", "Imane", 5000, employes_supervises)

    print(manager1.afficher_informations())

    manager1.ajouter_employe(employe3)

    print(manager1.afficher_employes_supervises())
