class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    # Méthodes getter et setter
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom.capitalize()

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom.capitalize()

    # Avec property
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            raise ValueError("L'âge doit être un entier positif")

if __name__ == "__main__":

    # La création d'une instance
    personne = Personne("Goussa", "Oussama", 21)

    # Accès aux attributs avec getter/setter et property
    print(f"Nom : {personne.get_nom()}, Prenom : {personne.get_prenom()}, Age : {personne.age}")

    personne.set_nom("Hakimi")
    personne.set_prenom("Ali")
    personne.age = 31

    print(f"Nom : {personne.get_nom()}, Prenom : {personne.get_prenom()}, Age : {personne.age}")

    # Erreur avec property
    try:
        personne.age = -1
    except ValueError as e:
        print(e)

