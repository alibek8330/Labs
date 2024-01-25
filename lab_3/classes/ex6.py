def primes(num):
  num = int(num)
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True
    
string = input()
numbers = string.split()
for i in numbers:
  i = int(i)

prime_numbers = list(filter(lambda x: primes(x), numbers))
prime_numbers = set(prime_numbers)

print(prime_numbers)