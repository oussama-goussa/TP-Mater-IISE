class NegativeAgeError(Exception):
  pass

def set_age(age):
  if age < 0:
    raise NegativeAgeError("L'âge ne peut pas être négatif.")
  else:
    print("L'âge a été défini avec succès.")

try:
  set_age(-5)
except NegativeAgeError as e:
  print(f"Une erreur s'est produite : {e}")

try:
  set_age(5)
except NegativeAgeError as e:
  print(f"Une erreur s'est produite : {e}")

