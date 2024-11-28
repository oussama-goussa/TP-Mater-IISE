def analyse_texte(texte):

    dictionnaire  = {}
    
    mots = texte.split()
    
    nombre_mots = len(mots)
    nombre_caracteres = len(texte.replace(" ", ""))
    
    dictionnaire ["nombre mots"] = nombre_mots
    dictionnaire ["nombre caracteres"] = nombre_caracteres

    return dictionnaire

texte = "Bonjour Oussama!"
print(analyse_texte(texte))