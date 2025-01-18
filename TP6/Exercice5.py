def process_input(user_input):
    try:
        number = int(user_input)
        result = number / 10
        return f"Le résultat de la division est : {result}"

    except ValueError:
        return "Veuillez entrer un nombre entier valide."

    except ZeroDivisionError:
        return "Division par zéro impossible."

print(process_input("100"))
print(process_input("abc"))
print(process_input("0"))