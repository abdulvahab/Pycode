# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual Pet"""
    # the constructor () method
    def __init__(self,name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    # the __pass_time() method      
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        
    # the mood property
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    # the talk() method
    def talk(self):
        print("I'm",self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
            
    # the eat() method
    def eat(self, food=0):
        food = int(input("Enter food fed in portion: ") )              
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            self.__pass_time()

    # the play() method
    def play(self, fun=0):
        fun = int(input("Enter hrs played: "))
                
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
            self.__pass_time()

# the main() function
def main():
    crit_name = input("What do you want to name your critter?: ")
    f = int(input("Enter food fed in portion: ") )
    p = int(input("Enter hrs played: "))
    crit = Critter(crit_name)
    
# Creating Menu
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker
        
        0 = Quit
        1 = Listen to your critter
        2 = Feed your critter
        3 = Play with your critter
        """)

        choice = input("Choice: ")
        print()

                # exit
        if choice =="0":
            print("Good-bye.")

                # listen to your critter
        elif choice =="1":
            crit.talk()

                # feed your critter
        elif choice =="2":
            food = int(input("Enter food fed in portion: ") )
            crit.eat()

                # play with your critter
        elif choice == "3":
            fun = int(input("Enter hrs played: "))
            crit.play()

                # Some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")
                    
# Starting the progamme
main()
("\nPress the enter key to exit.")


                
                
            
    
            
