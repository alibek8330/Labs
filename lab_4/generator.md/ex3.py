def by_3_4(n):
  for i in range(0, n):
    if i % 3 == 0 and i % 4 == 0:
      print(i, end = ' ')

n = int(input())
by_3_4(n)