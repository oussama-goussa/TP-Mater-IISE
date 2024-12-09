class Livre:
    def __init__(self ,titre ,auteur ,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return "'{}' par {} (Publié en {})".format(self.titre,self.auteur,self.annee_publication)

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self ,livre):
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :")
            for livre in self.livres:
                print("-",livre)

livre1 = Livre("À la recherche du temps perdu","Marcel Proust",1913)
livre2 = Livre("Don Quichotte","Miguel de Cervantes",1605)
livre3 = Livre("1984","George Orwell",1949)
livre4 = Livre("Le Vieil Homme et la Mer","Ernest Hemingway",1952)

biblio1 = Bibliotheque()

biblio1.ajouter_livre(livre1)
biblio1.ajouter_livre(livre2)
biblio1.ajouter_livre(livre3)
biblio1.ajouter_livre(livre4)

biblio1.afficher_livres()