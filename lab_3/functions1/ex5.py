from itertools import permutations

def get_permutations(string):
  perms = permutations(string)
  perm_list = [''.join(p) for p in perms]
  return perm_list

string = input()
result = get_permutations(string)

for perm in result:
  print(perm)