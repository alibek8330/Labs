import re
def splitString(string):
  x = re.findall("[A-Z][^A-Z]*", string)
  print(x)
splitString(input())