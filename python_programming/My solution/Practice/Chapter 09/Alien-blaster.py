# Alian Blaster programme
# Demostrates Object interaction

class Player(object):
    """A Player in Shooter game"""
    def blast(self,enemy):
        print("The player blast an enemy.\n")
        enemy.die()

class Alien(object):
    """An Alien in shooter game"""
    def die(self):
        print("The alien gasps and says,'Oh this is it. This is the big one.\n"\
              "Yes, it's getting dark now. Tell my 1.6 million larvae that"
               "I loved them...\n"\
              "Good-bye, cruel universe.'")
    
# main
print("\t\tDeath of an Alien\n")

hero = Player()
invader =Alien()
hero.blast(invader)

input("\nPress the enter key to exit")
