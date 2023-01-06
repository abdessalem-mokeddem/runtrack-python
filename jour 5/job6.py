def round_grades(grades):
  
  rounded_grades = []
  
  
  for grade in grades:
    
    if grade < 40:
      rounded_grades.append(grade)
    
    else:
      
      next_multiple = ((grade // 5) + 1) * 5
      
      if next_multiple - grade < 3:
        
        rounded_grades.append(next_multiple)
      
      else:
        
        rounded_grades.append(grade)
  
  
  return rounded_grades

print(round_grades([82, 83, 87, 88]))
print(round_grades([32, 35, 37, 38]))
print(round_grades([40, 43, 47, 48]))
print(round_grades([80, 83, 87, 88]))