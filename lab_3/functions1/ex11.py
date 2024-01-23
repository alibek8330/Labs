def palindrome(string):
  result = False
  reversed = string[::-1]
  if reversed == string:
    result = True
  return result

string = input()
print(palindrome(string))