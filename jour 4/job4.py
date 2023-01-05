def add_fruit_at_index():
  fruits = ["pomme", "cerise", "orange", "melon"]
  fruits.insert(2, "mangue")
  return fruits

fruits = add_fruit_at_index()
print(fruits)