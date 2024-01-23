def check(string):
  list = string.split()
  result = False
  for i in range(len(list) - 1):
    if list[i] == '0':
      if list[i+1] == '0':
        if list[i+2] == '7':
          result = True
          break
  return result

string = input()
print(check(string))