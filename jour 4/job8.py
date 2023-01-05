L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

total = 0
for element in L:
  if element % 2 == 0:
    total += element

print(f"La somme des valeurs paires de la liste L est {total}.")