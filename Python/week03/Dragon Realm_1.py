import time
import random

prize = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠟⠛⠋⠉⠉⠉⠉⠉⠙⠛⠓⠿⠿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠞⠋⢁⡀⠤⠀⠒⠀⠀⠀⠐⠒⠠⢀⠢⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⣿⠽⠛⠃⣀⠔⠉⠀⠀⠀⠀⢀⣀⣀⣤⣤⠤⠤⠄⠈⠀⠑⢀⡀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠿⠛⠿⠛⠃⠀⠀⡁⠁⠀⢀⣠⣴⣾⡿⠛⠉⠁⠀⠀⠀⠀⣀⢴⠤⢄⡀⠀⠀⠀⠀⠀⠀⠈⠻⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⡿⢦⠀⠀⠀⠀⠄⠀⠀⠀⠀⢀⣴⣿⣫⠤⠔⠚⠛⠒⠒⠚⠛⠯⠙⠢⡕⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⡇⠘⡄⠀⠀⠈⠀⠀⠀⠠⢴⡾⠛⠁⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠄⠚⠦⢀⣀⣧⠤⠔⠒⠛⣉⣉⣉⣉⣉⣉⣉⡁⢻⣦⡀⠀⠀⠄⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⠁⢀⠤⠒⣉⡥⠴⠖⢛⡯⣍⠉⢉⠤⢤⡀⢀⠬⣍⢉⠿⢿⣦⡀⠈⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿
⡇⠠⣡⢴⡟⠓⠦⡀⣰⠃⠀⠈⠳⠁⠀⠀⠻⠃⠀⠘⠋⠀⠀⠷⠓⡀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿
⣷⣾⠣⡾⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⢀⠀⠀⠀⠀⠀⠀⠆⠘⡄⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⢀⠀⣀⣼⣆⠈⢧⡀⠀⠀⠀⠀⠸⠀⢹⡀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⠀⠀⠀⢀⣀⢠⠤⠐⠶⠂⠐⠒⠈⢹⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢗⠀⠀⠀⠀⠀⣇⠀⢇⠀⠀⠀⠀⡷⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⣄⣌⠀⠀⠀⠀⠀⣀⣀⣤⣄⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢆⠀⠀⠀⠀⢸⠀⠘⠀⠀⠀⠀⣁⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⡿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢾⡄⠀⠀⠘⡇⠀⠀⠀⠀⢰⣷⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⠇⠀⠀⠀⣧⠀⠀⠀⠀⣸⣻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣧⠀⠄⠀⠀⢠⠀⠀⢰⣠⣯⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢻⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠃⠀⠀⠀⠉⢻⣿⠀⠀⠀⠀⢸⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣠⠴⠟⢋⡁⠾⠿⠋⠙⠻⠋⠉⠉⠉⠀⠀⠀⠀⠀⢠⣀⣀⣠⠏⠀⡸⠀⠀⢸⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢱⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡖⠤⣤⣀⣼⡷⠞⢁⣠⣾⠃⠀⠀⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣗⡇⠀⣀⠀⠀⠀⠀⠀⢀⡀⠀⠀⣤⣀⠀⣰⣡⣴⠖⠻⣕⠀⢺⠻⠊⠁⠀⣠⣾⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠘⢧⡴⠛⣆⣠⠖⢄⣀⣞⣉⣲⡾⠵⠚⠋⠉⠐⠈⠀⠉⠛⠓⠀⠀⠒⠒⠿⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⡉⠛⠛⠛⢛⣛⣉⣩⣥⡄⠒⠂⠀⠀⠀⠁⠉⠀⢀⣠⣌⣷⣖⣤⣄⣀⠘⠻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣭⣭⣿⣿⣻⣿⣷⣷⣷⣶⣶⣶⣶⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣆⣬⣘⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣛⣿
"""
#--------
#def to delay print time
#delay  = 1
#def printScript(msg):
    #print(msg)
    #time.sleep(delay)
#printScript("You are in a land full of dragons. In front of you,")
#printScript("you see two caves. In one cave, the dragons is friendly")
#printScript("and will share his dragons with you. The other dragon")
#printScript("is greedy and hungry, and will eat you on sight")
#print()
#--------

#Introduction
print("Welcome to amuseum park!")


#Ask to play
print("Do you want to play a game? y/n")
yesno = input()

#Making another loop to check if the input is not n or y 
while True:
    if yesno == "y" or yesno == "n":
        break
    else:
        print("Please choose between y/n")
        yesno = input()

#------
#or we can do this instead
#while yesno != "y" and yesno != "n":
#print("Please choose between y/n")
#yesno = input()

#------------------
#If the player wants to play
if yesno == "y":
    print("Insert A COIN!")
    coins = int(input())
#----------------    

#if not
if yesno == "n":
    coins = 0


#As long as there are coins left
while coins > 0:
    print("==================")


    #Throw dices
    print("Eye of dice1...")

    #---------------- 
    #Make a delay
    #delay_count = 0
    #while delay_count < 12345678:
        #delay_count = delay_count + 1
    #----------------

    #Make a delay
    time.sleep(2)


    #Throw dices
    dice1 = random.randint(1, 3)
    print(dice1)


    #Throw dices
    print("Eye of dice2...")
    #Make a delay
    time.sleep(2)


    #Throw dices
    dice2 = random.randint(1, 3)
    print(dice2)


    #Throw dices
    print("Eye of dice3...")
    #Make a delay
    time.sleep(2)


    #Throw dices
    dice3 = random.randint(1, 3)
    print(dice3)
    #----------------------------------

    #Check if won
    if dice1 == dice2:
        if dice2 == dice3:
            print(prize)
            print("Jackpot!")
    #Use a coin
    coins = coins - 1
    print("Coins left")
    print(coins)
    
    #----------------
    #UI/UX
    #print("***********")
    #print("Dice Results")
    #print("[", dice1 , "] [", dice2, "] [", dice3, "]", sep= "")
    #print("***********")
    #----------------

    if coins > 0:
    #Ask agian
        print("Do you want to play a game? y/n")
        yesno = input()


    if yesno == "n":
        print("Okay Here's your change")
        print(coins)
        break

    if yesno == "y":
        print("Okay lets play again!")

        
    print("===================")

