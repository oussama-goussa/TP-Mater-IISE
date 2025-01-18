def safe_division(a, b):
  if b == 0:
    raise ZeroDivisionError("Division par zéro impossible.")
  else:
    return a / b

try:
    result = safe_division(5, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print("Division effectuée avec succès.")
finally:
    print("Fin de la fonction.")