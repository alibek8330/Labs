import math

n = int(input("enter the size of the list: "))
list = []
for i in range(n):
    m = int(input("enter elements: "))
    list.append(m)

result = math.prod(list)
print(result)
