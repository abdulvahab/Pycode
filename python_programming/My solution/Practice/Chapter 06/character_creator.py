# Charector creator game

character = []
points = 30

choice = None
while choice != "0" :
    print("""
                    Charactor Creator

                    0- exit
                    1-Gain attribute spending points
                    2-show attributes
                    3-exchange attribut with point
     """)
    choice =input("Choice:")
    print()
    #exit
    if choice =="0":
        print("Good bye.")

    #Buying attributes
    elif choice=="1":
        print("""
                    Charector Attributes

                    's'= Strength
                    'h'= Health
                    'w'= Wisdom
                    'd'= Desterity

            """)
        attributes={"s":"Strength","h":"Health","w":"Wisdom","d":"Dexterity"}
        if points > 0:
            user_input=input("which attribute you want to aquire:")
            attribute=attributes[user_input]
            spend = int(input("How much points you want to spend:"))
            entry = (spend,attribute)
            character.append(entry)
            points -= spend
        else:
            print("you don't have enough point to buy an attribute:")

    # display Character 
    elif choice == "2":
        print("\t  MY HERO\n")
        print("ATTRIBUTES\t POINTS")
        for entry in character:
            spend, attribute = entry
            print(attribute,"\t\t",spend)

     # exchanging attributes with points
    elif choice == "3":
        attribute=input("which attribute you want to give-up:")
        for entry in character:
            if attribute in entry:
                character.remove(entry)
                lost_attribute = entry[1]
                refund = int(entry[0])
                points += refund
            else:
                print("attribute not in the list:")
    #invalid choice
    else:
        print("Invalid Choice")
        
    print("\nPoints remainingis\n", points)
    print("\nyour Character look like this:\n\n",character)
    

print("\t\tthanks for playing, press the enter key to exit") 
    
                    

                    
                    
