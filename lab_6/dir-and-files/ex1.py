import os

needed_path = input()
list = []
for path in os.listdir(needed_path):
  list.append(path)

print(list)

