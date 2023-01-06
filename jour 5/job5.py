def calculate_distance(steps, step_height):
  
  distance = (2 * steps * step_height) / 100000
  result = f"Pour {steps} marches de {step_height} cm, le gardien parcourt {distance:.2f} m par semaine."
  
  return result


print(calculate_distance(100, 20))
print(calculate_distance(200, 15))
print(calculate_distance(500, 10))

# Il fera 100 mètres par semaines.