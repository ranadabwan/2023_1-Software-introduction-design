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

def casting_dice(dice_num):
    print("Casting Dice", dice_num, "...", sep="")
    time.sleep(2)
    dice_result = random.randint(1,3)
    print(dice_result)
    return dice_result

def get_yesno():
    print("You want to play a game? y/n")
    yesno = input


    while yesno != "y" and yesno != "n":
        print("Please choose between y/n")
        yesno = input()
    return yesno


#--------
#Declare flags
#Initialize flags
is_dice1_fixed = False
is_dice2_fixed = False
is_dice3_fixed = False


#Introduction
print("Welcome to amuseum park!")

yesno = get_yesno()


#--------
#Ask to play
#print("Do you want to play a game? y/n")
#yesno = input()
#--------


#--------
#Making another loop to check if the input is not n or y
#while True:
    #if yesno == "y" or yesno == "n":
        #break
    #else:
        #print("Please choose between y/n")
        #yesno = input()
#--------

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


    if not is_dice1_fixed:
        #Throw dices
        dice1 = casting_dice(1)
        #print("Eye of dice1...")


        #Throw dices
        #dice1 = random.randint(1, 3

        #---------------- 
        #Make a delay
        #delay_count = 0
        #while delay_count < 12345678:
            #delay_count = delay_count + 1

        #Make a delay
        #time.sleep(2)
        #print(dice1)
        #----------------

    if not is_dice2_fixed:
        dice2 = casting_dice(2)
        #Throw dices
        #print("Eye of dice2...")
        #Make a delay
        #time.sleep(2)


        #Throw dices
        #dice2 = random.randint(1, 3)
        #print(dice2)

    if not is_dice3_fixed:
        dice3 = casting_dice(3)
        #Throw dices
        #print("Eye of dice3...")
        #Make a delay
        #time.sleep(2)


        #Throw dices
        #dice3 = random.randint(1, 3)
        #print(dice3)
        #----------------------------------

    #Check if won
    #----------------
    #if dice1 == dice2:
        #if dice2 == dice3:
    #----------------
    if dice1 == dice2 and dice2 == dice3:
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


    #0 to not fixed, 1 to fixed
    is_dice1_fixed = False
    is_dice2_fixed = False
    is_dice3_fixed = False

    
    fixing_dice_number = "-1"
    while fixing_dice_number != "n":
        print("Enter the number of dice you do not wish to change and want to carry on with to this next round then hit 'n' to quit fix mode.")
        fixing_dice_number = input()
        if fixing_dice_number == str(1):
            is_dice1_fixed = True
        if fixing_dice_number == str(2):
            is_dice2_fixing = True
        if fixing_dice_number == str(3):
            is_dice3_fixed = True

    if coins > 0:
    #Ask agian
        #print("Do you want to play a game? y/n")
        #yesno = input()

        yesno = get_yesno()


    if yesno == "n":
        print("Okay Here's your change")
        print(coins)
        break

    if yesno == "y" and coins == 0:
        print("Sorry, but you dont have enough coins..")
        break

    if yesno == "y":
        print("Okay lets play again!")

        
    print("===================")

