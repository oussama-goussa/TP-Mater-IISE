def fusionner_dicts(dict1, dict2):
    d = dict1.copy()

    for cle,valeur in dict2.items():
        if cle in d:
            d[cle] += valeur
        else:
            d[cle] = valeur
    
    return d

dict1 = {"a": 12, "b": 2, "c": 38}
dict2 = {"b": 15, "c": 2, "d": 49, "e": 7}

print(fusionner_dicts(dict1, dict2)) 