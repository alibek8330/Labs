n = int(input('Enter the size for your tuple: '))
input_tuple = ()
for i in range(n):
  t = input('Enter the tuple element: ')
  t = False if t == 'False' else t
  input_tuple += (t,)

result = all(input_tuple)
print(result)