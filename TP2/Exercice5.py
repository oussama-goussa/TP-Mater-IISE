class Animal:
    def faire_du_bruit(self):
        return "L'animal fait un bruit."
    
class Chien(Animal):
    def faire_du_bruit(self):
        return "Woof!"

class Chat(Animal):
    def faire_du_bruit(self):
        return "Miaou!"
    
chien1 = Chien()
chat1 = Chat()

print("Le chien fait un bruit:",chien1.faire_du_bruit())
print("Le chat fait un bruit:",chat1.faire_du_bruit())