# Guess my number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and computer lets
# the player know if the guess is too high or too low
# or right on the money

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attemts as possible.\n")

# define aask_number()
def ask_number(n):
    n = int(input("Guess my number: "))
    return n

# Set the initial values

tries = 1
the_number = random.randint(1,100)
guess = int(input("Take a guess:"))
ask_number(guess)

# gussing loop

while tries < 10 :
    if guess == the_number:
        break
    elif guess > 100:
        print("invalid number")
    elif guess > the_number :
        print("Lower...")
    elif guess < the_number :
        print("Higher...")        

    tries += 1
    guess =int(input("take a guess:"))

# result

if guess == the_number:
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")
else:
    print("you exited maximum number of tries, better luck next time, by the way the number was:", the_number)



input("\n\nPress the enter key to exit.")


        

            
