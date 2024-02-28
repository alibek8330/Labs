import re
def spaces(string):
  x = re.sub("(.)([A-Z])", r"\1 \2", string)
  print(x)
spaces(input())