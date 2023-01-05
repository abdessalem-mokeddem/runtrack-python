def swap_first_last(lst):
  if len(lst) > 0:
    lst[0], lst[-1] = lst[-1], lst[0]
  return lst

# Exemple d'utilisation de la fonction
lst = [1, 2, 3, 4, 5]
swap_first_last(lst)
print(lst)