#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)


def fahrenheit_to_centigrade(temp):
  celcia = (5.0/9.0) * (temp - 32)
  return celcia

temp = int(input())
print(fahrenheit_to_centigrade(temp), end = "")
print("C")