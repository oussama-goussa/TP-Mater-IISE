def get_positive_integer():
    while True:
        try:
            user_input = input("Veuillez saisir un entier positif : ")
            number = int(user_input)
            
            if number <= 0:
                print("L'entier doit être positif. Essayez encore.")
            else:
                return number
        except ValueError:
            print("Entrée invalide. Veuillez saisir un entier.")

result = get_positive_integer()
print("Vous avez saisi :", result)