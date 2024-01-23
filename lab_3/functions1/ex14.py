import time

def draw_tree(number):
  for i in range(1, number + 1):
    for j in range(number - i):
      print(" ", end="")
    for k in range(2 * i - 1):
      print("*", end="")
    print()

import random
print("Hello! What is your name?")
name = input()
random_number = random.randint(1, 20)
condition = False
count = 0
print("Well, " + name + ", let's play a game.")
time.sleep(1)
print("I guess one number and then we will build x-mas by this size")
time.sleep(1)
print("Take a guess")
number = int(input())
while condition is False:
  count += 1
  if number == random_number:
    print("Good job, " + str(name) + "! You guessed my number in " + str(count) + " guesses!")
    time.sleep(1)
    print("Well done!")
    condition = True
  if number < random_number:
    print("Your guess is too low.")
    time.sleep(1)
    print("Take a guess")
    number = int(input())
  if number > random_number:
    print("Your guess is too high.")
    time.sleep(1)
    print("Take a guess")
    number = int(input())
    
    
if condition is True:
  print("Let's build our x-mas")
  draw_tree(number)

print("Finally, the last game")
time.sleep(1)
print("I will show you my magic special super puper duper mega ultra ability")
time.sleep(1)
print("Say something")
word = input()
drow = word[::-1]
print(drow)
print("UHAAHAHAHAH Did you show?")
time.sleep(1)
print("Lets do it again")
time.sleep(1)
print("Say something again")
time.sleep(1)
word = input()
drow = word[::-1]
print(drow)
print("IIIEEEEUHHHH")
time.sleep(1)
print("Lets repeat it finally")
word = input()
drow = word[::-1]
print(drow)
print("UUUUHUUUUUU AHAHAH")
time.sleep(1)
print("OK buddy thank you that you give me possibility to show it")
time.sleep(1)

print("My second ability is converting units")
time.sleep(2)
print("For example converting km to miles")
time.sleep(2)
print("Now write some number")
number = int(input())
result = number * 0.621371
print(f"{number} km is {result} miles")
time.sleep(2)
print("That's all")
time.sleep(2)
print("There was funny!")
time.sleep(2)
print("Thank for your attention")
time.sleep(2)
print("Good bye, good luck")
time.sleep(2)
print("See you soon")

