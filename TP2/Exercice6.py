class Rectangle:
    def __init__(self ,largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur
    
    def calculer_perimetre(self):
        return (self.largeur + self.hauteur)*2
    
r1 = Rectangle(5,8)

print("La surface du rectangle est:", r1.calculer_surface())
print("La périmètre du rectangle est:", r1.calculer_perimetre())