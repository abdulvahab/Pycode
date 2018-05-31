# Guess the word
#
# best of luck

import random

WORDS = ("fatema", "abdulrehman", "computer", "misbah","aaliyah")
word = random.choice(WORDS)
correct = word
l=len(word)
print("It's a", l, "letter Word: ","*"*l)
guess_letter = 5


# Guess your letter to understand the word
letters = ()
print("\t\tlet's guess the letter in the word:")
while guess_letter != 0:
    guess =input("Guess your letter:")
    if guess in word:
        letters += tuple(guess)
        guess_letter -= 1 
        print("yes this letter is in the word:")
    else:
        print("No, this letter is not in the word:")
        guess_letter -= 1
print("letters in the words are : ", letters)

# Guess your word now
guess_word_count = 3
print("\t\tlet's guess the word now")

while guess_word_count != 0:
    guess_word = input("Guess your word:")
    if guess_word == correct:
        print("\nyou guessed it, well done")
        break
    else:
        print("\HOH OH :")
        guess_word_count -= 1
       

input("\n\n\nyTHanks for plying")






