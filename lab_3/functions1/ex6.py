def reverse(string):
  words = string.split()
  reversed_string = ' '.join(reversed(words))
  return reversed_string

string = input() 
print(reverse(string))
