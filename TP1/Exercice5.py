def factorielle(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)
    
n = int(input("Entez un nombre entier: "))
print(factorielle(n))