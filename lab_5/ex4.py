import re
pattern = "[A-Z][a-z]+"
string = re.findall(pattern, input())
print(string)