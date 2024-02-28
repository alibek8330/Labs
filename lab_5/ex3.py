import re
pattern = "[a-z]+_[a-z]+"
string = re.findall(pattern, input())
print(string)