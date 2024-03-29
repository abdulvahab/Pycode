# word jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# Create a sequence of words to choose from

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomely from sequence

word =random.choice(WORDS)
hint_word = word[0:len(word)-2]


# create a variable to use later to see if the guess is correct
correct = word

# Create a jumbled version of the word
jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
    
   
# start the game

print(
"""
            Welcome to Word Jumble!

        Unscramble the letters to make a word.
        (press the key at the promt to quit.)
"""
)
print("The jumble is:",jumble)

guess = input("\nYour guess:")

penalty = 0
chance = 10
while guess != correct and chance != 0:
    chance = 10 -penalty
    print("Sorry, that's not it.")
    print("Do you need help:")
    response = input("y or n:")
   
    
    if response == 'n':
        penalty += 0
        
    elif response == "y":
        print("the hint is :", hint_word)
        penalty += 1  
                          
    print("Penalty so far:",penalty)
    print("chance remaining:",10-penalty)
    guess= input("Your guess: ")
    

if guess == correct:
    print("That's it! You guessed it!\n")
print("your score is ",chance*100)

print("thanks for playing")

input("\n\nPress the enter key to exit.")

    
    
