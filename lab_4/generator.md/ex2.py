def generator_evens(n):
  for i in range(1, n+1):
    if i % 2 == 0:
      print(i ** 2, end =',')

n = int(input())
generator_evens(n)