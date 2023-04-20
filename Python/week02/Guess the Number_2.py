import random


multiline = """

 .-------.
                              |Jackpot|
                  ____________|_______|____________
                 |  __    __    ___  _____   __    |  
                 | / _\  / /   /___\/__   \ / _\   | 
                 | \ \  / /   //  //  / /\ \\ \  25|  
                 | _\ \/ /___/ \_//  / /  \/_\ \ []| 
                 | \__/\____/\___/   \/     \__/ []|
                 |===_______===_______===_______===|
                 ||*|\_     |*| _____ |*|\_     |*||
                 ||*|| \ _  |*||     ||*|| \ _  |*||
                 ||*| \_(_) |*||*BAR*||*| \_(_) |*||
                 ||*| (_)   |*||_____||*| (_)   |*|| __
                 ||*|_______|*|_______|*|_______|*||(__)
                 |===_______===_______===_______===| ||
                 ||*| _____ |*|\_     |*|  ___  |*|| ||
                 ||*||     ||*|| \ _  |*| |_  | |*|| ||
                 ||*||*BAR*||*| \_(_) |*|  / /  |*|| ||
                 ||*||_____||*| (_)   |*| /_/   |*|| ||
                 ||*|_______|*|_______|*|_______|*||_//
                 |===_______===_______===_______===|_/
                 ||*|  ___  |*|   |   |*| _____ |*||
                 ||*| |_  | |*|  / \  |*||     ||*||
                 ||*|  / /  |*| /_ _\ |*||*BAR*||*||              
                 ||*| /_/   |*|   O   |*||_____||*||        
                 ||*|_______|*|_______|*|_______|*||
                 |lc=___________________________===|
                 |  /___________________________\  |
                 |   |                         |   |
                _|    \_______________________/    |_
               (_____________________________________)

               """
#Your fancy greetings
print("Hello, Welcome to Jackpot Game!")
print("Enter the number of coins: ")

#------------------
#print("You want to play a game? y/n")
#get yes or no
#yesno = input()
#------------------

coins = input()
coins = int(coins)

#------------------
#if yes
#while yesno == "y":
#------------------


while coins > 0 :
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

    
    print("The dice is casting. . .")
    #Make a delay
    delay_count = 0
    while delay_count < 12345678:
        delay_count = delay_count + 1



    #Compare two dices
    #Usig if condition
    if dice1 ==  dice2:
        if dice2 ==  dice3:
            #Print result
            print("Jackpot!")

    coins = coins - 1
    print("Coins left")
    print(coins)

    #------------------
    #Ask again
    #print("Okay, you want to throw dices again?")
    #roll_again = input
    #------------------
