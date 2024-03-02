string = input("enter a string: ")
reversed_string = ''.join(reversed(string))
if string == reversed_string:
  print("the string is a palindrome.")
else:
  print("the string is not a palindrome.")