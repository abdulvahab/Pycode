# Hero's Inventory
# Demostrates tuple creation

# Create an empty tuple
inventory = ()

# Treat tuple as a condidion
if not inventory:
    print("you are empty handed:")

input("\n\nPress the enter key to continue.")

# Create a tuple with some items
inventory = ("sword", "armor","Shield","healing potion")

# print the tuple
print("\nyour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")
    
