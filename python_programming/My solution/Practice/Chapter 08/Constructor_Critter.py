# Constructor Critter
# Demostrates Constructors

class Critter(object):
    """A virtual Pet"""
    def __init__(self):
        print("A new critter has been born!")

    def talk(self):
        print("\n\n I am an instance of class Critter.")

# main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit.")
