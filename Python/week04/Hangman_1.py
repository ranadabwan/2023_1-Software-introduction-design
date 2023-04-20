#Display ASCII HANGMAN

import random

def getSecretWord(words):
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    return category, word

def displayASCII(remained):
    lastIndex = len(HANGMANPICS) - 1
    print(HANGMANPICS[lastIndex - remained])

def displaySecretWord(secretWord, guesses):
    displayed = ''
    for letter in secretWord:
        if letter in guesses:
            displayed += letter + ' '
        else:
            displayed += '_ '
    print(displayed)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = {"Colors": '''red orange yellow green blue indigo 
violet white black brown'''.split(), "Shapes": '''
square triangle rectangle circle ellipse 
rhombus trapazoid chevron pentagon hexagon septagon octogon
'''.split(), "Fruit": '''apple orange lemon lime pear watermelon 
grape grapefruit cherry banana cantalope mango straberry tomato
'''.split(), "Animals": '''ant baboon badger bat bear beaver camel 
cat clam cougar coyote crew deer dog donkey duck eagle ferret 
fox frog goat goose hawk lion lizard llama mole monkey moose 
mouse mule newt otter owl panda parrot pigeon rabbit ram rat 
raven rhino salmon seal shark sheep skunk sloth snake spider 
stork swan tiger toad trout turkey turtle whale wolf wombat zebra
'''.split()}

playAgain = True
while playAgain:
    remained = 6
    category, secretWord = getSecretWord(words)
    letters = list(secretWord)
    guesses = []

    while len(letters) > 0 and remained > 0:
        displayASCII(remained)
        displaySecretWord(secretWord, guesses)
        guess = input()
        guess = guess.lower()
        if guess in guesses:
            print("You have typed the letter: " + guess)
        elif guess in letters:
            guesses.append(guess)
            pos = letters.index(guess)
            del letters[pos]
        else:
            remained = remained - 1

        if remained == 0:
            displayASCII(remained)
            print("The secret word was... " + secretWord)

        if len(letters) == 0:
            print("Congratulations! You guessed the secret word.")
            print("The secret word was... " + secretWord)

        print("Do you want to play again? (yes or no)")
        answer = input()
        if answer != "yes":
            playAgain = False
