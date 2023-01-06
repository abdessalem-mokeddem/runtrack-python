def tapis(n):
  for i in range(n + 1):
    for j in range(n + 1):
      if i == j:
        print("X", end=" ")
      else:
        print("O", end=" ")
    print()