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
#Declare flags
#Initialize flags
#is_dice1_fixed = False
#is_dice2_fixed = False
#is_dice3_fixed = False


#is_dice_fixed = [False, False, False]
#eye_of_dice = [-1, -1, -1]
#--------

NUM_DICE = 3

is_dice_fixed = []
eye_of_dice = []
for dice_num in range(NUM_DICE):
    is_dice_fixed.append(False)
    eye_of_dice.append(-1)



    
def casting_dice(dice_num):
    print("Casting Dice", dice_num, "...", sep="")
    time.sleep(2)
    dice_result = random.randint(1,3)
    #print(dice_result)
    return dice_result

def get_yesno():
    print("You want to play a game? y/n")
    yesno = input()


    while yesno != "y" and yesno != "n":
        print("Please choose between y/n")
        yesno = input()
    return yesno


#--------
#Declare flags
#Initialize flags
#is_dice1_fixed = False
#is_dice2_fixed = False
#is_dice3_fixed = False


is_dice_fixed = [False, False, False]
eye_of_dice = [-1, -1, -1]


#Introduction
print("Welcome to amuseum park!")

yesno = get_yesno()

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


    for dice_index in range(NUM_DICE):
        if not is_dice_fixed[dice_index]:
            eye_of_dice[dice_index] = casting_dice(dice_index)

    

    #if not is_dice_fixed[0]:
        #Throw dices
        #eye_of_dice[0] = casting_dice(0)
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

    #if not is_dice_fixed[1]:
        #eye_of_dice[1] = casting_dice(1)


        
        #dice2 = casting_dice(2)
        #Throw dices
        #print("Eye of dice2...")
        #Make a delay
        #time.sleep(2)


        #Throw dices
        #dice2 = random.randint(1, 3)
        #print(dice2)

    #if not is_dice_fixed[2]:

        #eye_of_dice[2] = casting_dice(2)

        
        #dice3 = casting_dice(3)
        #Throw dices
        #print("Eye of dice3...")
        #Make a delay
        #time.sleep(2)


        #Throw dices
        #dice3 = random.randint(1, 3)
        #print(dice3)
        #----------------------------------
    print("[ ", eye_of_dice[0], "] [ ", eye_of_dice[1], "] [ ", eye_of_dice[2], "]", sep="")



    
    #Check if won
    #----------------
    #if dice1 == dice2:
        #if dice2 == dice3:
    #if dice1 == dice2 and dice2 == dice3:
    #----------------

    if eye_of_dice[0] == eye_of_dice[1] and eye_of_dice[1] == eye_of_dice[2]:
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

    #----------------
    #0 to not fixed, 1 to fixed
    #is_dice1_fixed = False
    #is_dice2_fixed = False
    #is_dice3_fixed = False
    #----------------



    is_dice_fixed = []
    for i in range(NUM_DICE):
        is_dice_fixed.append(False)


    #is_dice_fixed = [False, False, False]
        

    
    fixing_dice_number = "-1"
    dice_list = []

    for dice_index in range(NUM_DICE):
        dice_list.append(str(dice_index))

        
    while fixing_dice_number != "n":
        print("Enter the number of dice you do not wish to change and want to carry on with to this next round then hit 'n' to quit fix mode.")
        fixing_dice_number = input()
        if fixing_dice_number in dice_list:
            is_dice_fixed[int(fixing_dice_number)] = True

        
        #if fixing_dice_number == str(1):
            #is_dice1_fixed[0] = True
            #is_dice1_fixed = True

            
        #if fixing_dice_number == str(2):
            #is_dice2_fixing[1] = True

            
        #if fixing_dice_number == str(3):
            #is_dice3_fixed[2] = True

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

