def mot_plus_loin(mot):
 mot_trié = sorted(mot)

  
for i, c in enumerate(mot_trié):
    if c != mot[i]:
   
      mot_trié[i] = mot[i]
      break
  
  return "".join(mot_trié)

mot = input("Entrez un mot : ")

    print(mot_plus_loin(mot))



