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

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'a pas été trouvé.")
        return None
    except IOError:
        print(f"Erreur : Impossible de lire le fichier '{filename}'.")
        return None

def main():
    filename = input("Veuillez saisir le nom du fichier à lire : ")
    file_content = read_file(filename)
    
    if file_content:
        print("Fichier lu avec succès.")
        print(file_content)
        
        number = get_positive_integer()
        print(f"Vous avez saisi le nombre : {number}")
    else:
        print("Impossible de continuer sans le fichier valide.")

if __name__ == '__main__':
    main()
