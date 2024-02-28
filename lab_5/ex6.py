import re
text = input()
string = re.sub(r"\s|\,|\.", ":", text)
print(string)