L = [8, 24, 48, 2, 16]

count = 0
for element in L:
  if element % 3 == 0:
    count += 1

print(f"Il y a {count} multiples de 3 dans la liste L.")