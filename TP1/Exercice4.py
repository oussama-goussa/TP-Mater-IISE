def compte_occurences(liste):
    dictionnaire  = {}
    
    for mot in liste:
        if mot in dictionnaire :
            dictionnaire [mot] += 1
        else:
            dictionnaire [mot] = 1
            
    return dictionnaire 

liste = ['ali', 'omar', 'ali', 'salma', 'omar', 'omar', 'ali', 'Oussama']
print(compte_occurences(liste))