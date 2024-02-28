import re
pattern = "ab*"
x = re.search(pattern, input())
if x:
  print(True)
else:
  print(False)