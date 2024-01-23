#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
  numheads *= 4
  numlegs *= 2
  rab_legs = numlegs - numheads
  rab_heads = rab_legs / 4
  numlegs /= 2
  chic_legs = numlegs - rab_legs
  chic_heads = chic_legs / 2
  return int(rab_heads), int(chic_heads)

numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))

