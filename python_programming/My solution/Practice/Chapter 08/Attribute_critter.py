# Attribute Critter
# Demostrates creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self,name):
        print("The new object has been created\n")
        self.name = name
    def __str__(self):
        rep = "Critter object\n"
        rep += "name :"+ self.name + "\n"
        return rep
    def talk(self):
        print("Hi., I'm", self.name,"\n")

# main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1: ")
print(crit1)

print("Directely accessing crit1.name:")
print(crit1.name)

input("\n\nPress the enter key to exit.")
              
