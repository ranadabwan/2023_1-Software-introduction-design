import random

#Your fancy greetings
print("Hello, Welcome to Jackpot Game!")

#Throw dice
print("==============")
dice2 = random.randint(1, 3)
dice1 = random.randint(1, 3)
dice3 = random.randint(1, 3)

print("Eye of the dice1: ")
print(dice1)
print("Eye of the dice2: ")
print(dice2)
print("Eye of the dice3: ")
print(dice3)
print("===============")



#Compare two dices
#Usig if condition
if dice1 ==  dice2:
    if dice2 ==  dice3:
        #Print result
        print("Jackpot!")
