import random
print("Hello! What is your name?")
name = input()
random_number = random.randint(1, 20)
condition = False
count = 0
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
print("Take a guess")
number = int(input())
while condition is False:
  count += 1
  if number == random_number:
    print("Good job, " + str(name) + "! You guessed my number in " + str(count) + " guesses!")
    condition = True
  if number < random_number:
    print("Your guess is too low.")
    print("Take a guess")
    number = int(input())
  if number > random_number:
    print("Your guess is too high.")
    print("Take a guess")
    number = int(input())
  

