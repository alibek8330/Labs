import os

file_path = input()
with open(file_path, "r") as file:
  lines = len(file.readlines())
  print("number of lines", lines)
