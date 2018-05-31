# TV 2.0
# Demostrate module and class

import TV_module,games,random

class Housemate(object):
    def __init__(self,names):
        self.names = names
        
        print("<",count.index(i+1),"> :","Housemate is :", name)
    def concent(self):
        concent = None
        for name in self.names:
            concent = games.ask_yes_no("Do you want to Watch TV ?(y/n):")
            print(name)
            if concent == 'y':
                print("you are allowed 120 ,Be ready for your Turn")
            elif concent == 'n':
                print("Good night, Go to Bed")
            else:
                print("Press 'y' or 'n' to make a choice")        
        
names =[]
n = games.ask_number("How many Housemates:",1,6)
count = list(range(n+1))
for i in range (n):
    name = input("Enter name of Housemate:  ")
    names.append(name)
    h = Housemate(names)
    print()



input("\nPress the enter key to exit.")
    
      
    
    
    
    
    

