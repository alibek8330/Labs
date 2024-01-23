def double3(string):
  list = string.split()
  result = False
  for i in range(len(list) - 1):
    if list[i+1] == list[i]:
      result = True
      break
  return result

string = input()
print(double3(string))


