from abc import ABC,abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer():
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture roule.")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette pédale.")

if __name__ == "__main__":
    voiture1 = Voiture()
    voiture1.deplacer()

    bicyclette1 = Bicyclette()
    bicyclette1.deplacer()