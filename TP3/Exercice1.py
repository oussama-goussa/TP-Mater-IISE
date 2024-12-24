from abc import ABC,abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def calculer_surface():
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * (self.rayon**2)
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur
    
if __name__ == "__main__":

    cercle = Cercle(5)
    rectangle = Rectangle(4, 6)

    surface_cercle = cercle.calculer_surface()
    surface_rectangle = rectangle.calculer_surface()

    print(f"Surface du cercle : {surface_cercle:.2f}")
    print(f"Surface du rectangle : {surface_rectangle}")

