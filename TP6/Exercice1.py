def safe_division(a, b):
  if b == 0:
    raise ZeroDivisionError("Division par zéro impossible.")
  else:
    return a / b
  
try:
  result = safe_division(10, 2)
  print(result)  # Affiche 5
except ZeroDivisionError as e:
  print(e)  # Affiche "Division par zéro impossible."

try:
  result = safe_division(5, 0)
except ZeroDivisionError as e:
  print(e)