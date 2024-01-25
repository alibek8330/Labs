#separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def filter_prime(list):
  prime = []
  for i in list:
    i = int(i)
    if i > 1:
      for j in range(2, i):
        if i % j == 0:
          break
      else:
        prime.append(i)
  return prime

n = input()
list = n.split()
print(filter_prime(list))