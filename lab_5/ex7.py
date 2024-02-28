import re
def func(snakeText):
  regex = "^(\w+)\_(\w+)"
  match = re.search(regex, snakeText)
  if match:
    first = match.group(1)
    second = match.group(2)
    second = second[0].upper() + second[1:]
    camelText = first + second
    print(camelText)

func(input())