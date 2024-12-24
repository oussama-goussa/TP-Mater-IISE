from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * self.rayon**2
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur
    
def afficher_surface(formes):
    for forme in formes:
        print(f"La surface de {forme.__class__.__name__} est : {forme.calculer_surface():.2f}")

if __name__ == "__main__":
    cercle1 = Cercle(6)
    rectangle1 = Rectangle(6, 4)
    rectangle2 = Rectangle(2, 3)
    cercle2 = Cercle(3)

    formes = [cercle1, rectangle1, rectangle2, cercle2]

    afficher_surface(formes)