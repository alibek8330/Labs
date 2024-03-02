string = input("enter a string: ")
uppercases = 0
lowercases = 0
for i in string:
    if i.isupper():
        uppercases += 1
    if i.islower():
        lowercases += 1
print("uppercase letters: ", uppercases)
print("lowercase letters: ", lowercases)
