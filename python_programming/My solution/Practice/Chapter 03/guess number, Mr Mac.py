# Guess my number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and computer lets
#Computer Guess the User input
# the playe know if the guess is too high or too low
# or right on the money

import random

print("\tWelcome to 'Guess My Number'!, Mr. Mac")
print("\nI'm inputting  a number between 1 and 100.")
print("Mr Computer,Try to guess it in as few attemts as possible.\n")

# Set the initial values

tries = 0
the_number = int(input("My number is :"))
a = random.randint(1,100)
# gussing loop

while tries < 57:
    guess = a
    if guess == the_number:
        tries += 1
        break
    elif guess > the_number :
        print(guess,"Guess Lower...")
        tries += 1
        a = random.randint(1,(guess-1))        
        input("Press the enter for another guess.")
        continue
    elif guess < the_number :
        print(guess,"Guess Higher...")
        tries += 1                              
        a = random.randint((guess+1),the_number)     
        input("\Press the enter for another guess.")
        continue          
    

# result

if guess == the_number:
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")
else:
    print("you exited maximum number of tries, better luck next time, by the way the number was:", the_number)



input("\n\nPress the enter key to exit.")


        

            
