L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

product = 1
for element in L:
  if 25 <= element <= 90:
    product *= element

print(f"Le produit des valeurs de la liste L comprises dans l'intervalle [25, 90] est {product}.")
