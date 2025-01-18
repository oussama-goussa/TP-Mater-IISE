# Exercice7.py

import logging

logging.basicConfig(filename='TP6/error.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def log_error(message):
    logging.error(message)

def read_file(fichier):
    try:
        with open(fichier, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        log_error(f"File not found: {fichier}")
        return None

if __name__ == "__main__":
    
    fichier = 'TP6/data.txt'

    content = read_file(fichier)

    if content is None:
        print("Le fichier n'a pas été trouvé et l'erreur a été enregistrée.")
    else:
        print("Contenu du fichier :", content)