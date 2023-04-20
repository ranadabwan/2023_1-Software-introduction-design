# This is "Guess the number" game
import random

print("What is your name?")
myName = input()
number = random.randint(1, 20)
guessesTaken = 1

print("Well, " + myName + ".")
print("I am thinking of a number between 1 and 20.")

while guessesTaken < 6 :
    guess = input()
    guess = int(guess)
    if guess == number : 
        break
    guessesTaken = guessesTaken + 1
    if guess > number :
        print("Your guess is to high!")
    if guess < number :
        print("Your guess is to low!")

if guess == number :
    guessesTaken = str(guessesTaken)
    print("Good job, " + myName + "!")
    print("You guessed my number in " + guessesTaken + " guesses!")
if guess != number :
    number = str(number)
    print("Nope. The number was " + number)
