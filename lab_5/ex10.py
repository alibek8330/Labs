import re
def camelToSnake(camel_str):
  snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()
  print(snake_case)

camelToSnake(input())