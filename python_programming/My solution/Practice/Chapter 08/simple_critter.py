# Simple Critter
# Demostrates a basic class and object

class critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm an instance of class Critter.")

# main
crit = critter()
crit.talk()

input("\n\nPress the enter key to exit.")
