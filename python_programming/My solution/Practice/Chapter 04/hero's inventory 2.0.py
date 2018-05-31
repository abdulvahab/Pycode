# Hero's inventory 2.0
# Demostrates tuple

# Create a tuple with some items and dispaly with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print("Your items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to continue.")

print("You have ", len(inventory), "items in your possiossion.")

input("\n\nPress the enter key to continue.")

# Test membership with in
if "healing potion" in inventory:
    print("you will live to fight another day.")

# Display one item through an index

index = int(input("\nEnter the index number for an item in inventory:"))
print("At index", index, "is", inventory[index])

# Display a slice

start = int(input("\nEnter the index number to begin a slice:"))
finish = int(input("\nEnter the index number to end  a slice:"))
print("inventory[",start,":",finish, " ]")
print(inventory[start:finish])

input("\n\nPress the enter key to continue.")

# Concatenate two tuples
chest = ("gold","gems")
print("you find a chest. It contains:")
print(chest)

print("you add the contents of the chest to your inventory.")
inventory += chest

print("Your inventory is now:")
print(inventory)

input("\n\nPress the enter key to exit.")
      
