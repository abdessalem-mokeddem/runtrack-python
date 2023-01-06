def shift_message(message, shift):

  result = ''
  
  
  for c in message:
    
    if c.isalpha():
      
      c = c.upper()
      
      ascii_value = ord(c) + shift
      
      if ascii_value > ord('Z'):
        ascii_value -= 26
      elif ascii_value < ord('A'):
        ascii_value += 26
      
      c = chr(ascii_value)
    
    result += c
  
  return result

print(shift_message('Hello, World!', 3))
print(shift_message('Hello, World!', -5))
print(shift_message('Hello, World!', 26))
print(shift_message('Hello, World!', -26))