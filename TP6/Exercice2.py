def convert_to_int(value):
  try:
    return int(value)
  
  except ValueError:
    raise ValueError(f"Impossible de convertir '{value}' en entier.")
  
try:
  result = convert_to_int("42")
  print(result)
except ValueError as e:
  print(e)

try:
  result = convert_to_int("abc")
except ValueError as e:
  print(e)