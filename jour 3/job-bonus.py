def reverse_string(string):
  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string

original_string = "nikana"
reversed_string = reverse_string(original_string)

print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")