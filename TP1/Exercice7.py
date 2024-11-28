def salutation(nom, message="Bonjour"):
    return message+" "+nom

nom = input("Entez votre nom: ")
print(salutation(nom))