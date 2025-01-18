def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"Erreur : le fichier '{filename}' n'a pas été trouvé.")
    finally:
        try:
            file.close()
        except NameError:
            pass

filename = 'TP6/data.txt'
content = read_file(filename)
if content:
    print("Contenu du fichier :", content)