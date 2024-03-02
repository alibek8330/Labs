from time import sleep
import math

def sqrtfunc(sqrtfunc, ms, *args):
  sleep(ms / 1000)
  return sqrtfunc(*args)

n = int(input("Enter a number: "))
ms = int(input("Enter a number of milliseconds: "))
print("Square root after specific milliseconds:")
print(sqrtfunc(lambda x: math.sqrt(x), ms, n))
