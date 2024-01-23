def histogram(string):
  list = string.split()
  for i in list:
    i = int(i)
    print('*' * i)
string = input()
histogram(string)