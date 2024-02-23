def div_by_3and4(n):  
  x = 12
  while x <= n:
    yield x
    x += 12

[print(x, end=' ') for x in div_by_3and4(int(input()))]