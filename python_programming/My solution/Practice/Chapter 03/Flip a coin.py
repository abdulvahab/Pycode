# Flip a coin
import random

heads = 0
tails = 0

turn = 0

while turn < 100:
    flips = random.randint(1,2)
    
    if flips == 1:
        heads += 1
 
    else:
        tails += 1
    turn += 1

print("In 100 turns you have generated")
print("heads=",heads)
print("tails=",tails)
        
input('\n\nPress the enter key to exit.')


    
              
    
