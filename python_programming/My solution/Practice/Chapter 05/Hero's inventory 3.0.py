# hero's inventory 3.0
#
#Demostrates list
#Create a list with some items and display with a for loop
inventory=["sword","armor","shield","healing potion"]
print("your items:")
for item in inventory:
    print(item)

input("\n\npress the enter key to continue")

#get the length of the list

print("you have",len(inventory),"items in your possiosions")

#test membership with in

if "healing potion" in inventory:
    print("You will live to fight anothe day.")

#dispaly one item through an index
    
index=int(input("Enter the item number for an item in inventory:"))
print("At index",index, "is",inventory[index])

#display a slice
start =int(input("\nEnter the index number to begin a slice:"))
finish =int(input("\nEnter the index number to end a slice:"))

print("inventory[",start,



      ":" , finish, "] is", end=" ")
print(inventory[start:finish])

input("\n\npress the enter key to continue")

#concatenate two list
chest = ["gold","gems"]
print("you find the chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print(inventory)

input("\n\npress the enter key to continue")

#assign by index
print("you trade your sword for a crossbow")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

input("\n\npress the enter key to continue")

#assign by slice
print("you use your gold and gems to buy an orb of future telling.")
inventory[4:6] =["orb of future telling"]
print("Your inventory is now:")
print(inventory)

input("\n\npress the enter key to continue")

#delete an element
print("In a great battle your shiels is destroyed.")
del
inventory[2]
print("Your inventory now:")
print(inventory)

input("\n\npress the enter key to continue")

#delete a slice
print("Your crossbow and armor stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)

input("\n\npress the enter key to ecit.")
