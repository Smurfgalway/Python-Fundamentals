# Guessing Game (ex 5)
import random
secNum = random.randrange(1,11)
guess = 0
count = 0
print ("you have 10 guesses to get the number correct")
while (count < 10):
    guess = input("please make you guess a number between 1 and 10 ")
    if int(guess) > int(secNum):
        print("you went too high guess again")
        count += 1
        print("Guess ", count, " used")
    if int(guess) < int(secNum):
        print("you went too low guess again")
        count += 1
        print("Guess ", count, " used")
    if int(guess) == int (secNum):
        print ("you got it on guess", count, "well done!!")
        break
    