def squares(start, stop):
  while start <= stop:
    yield start**2
    start += 1

[print(x, end=' ') for x in squares(int(input()), int(input()))]