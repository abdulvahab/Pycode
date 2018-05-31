# Who's your Daddy
#
pair ={"aryan":"sharukh khan","abdulvahab":"abdulgafoor","abdulgafoor":"alimiya"}

choice = None
while choice != "0":
    
    print("""
                        DADDY'S NAME
                        -------------
                         0 - EXIT
                         1 - SHOW LIST
                         2 - ADD PAIR
                         3 - REMOVE PAIR
                         4 - REPLACE FATHER NAME

        """)
    choice = input("choice:")
    print()
    
    if choice =="0":
        print("Good Bye.")
        
    elif choice == "1":
        name = input("Enter person's name:")
        if name in pair:
            dad_name = pair[name]               
            print("NAME\t\tDADDY'S NAME")
            print(name,"\t", dad_name)
        else:
            print("name not known:")

    elif choice == "2":
        name =input("enter name of the person:")
        if name not in pair:
            dad_name =input("enter name of person's dad name:")
            pair[name] = dad_name
            print("pair has been added")
        else:
            ("The person name already in the pair, try to replace his father's name")
    elif choice =="3":
        name = input("which pair you want to delete:")
        if name in pair:
            del pair[name]
            print("\nOkay, I deleted", name)
        else:
            print("\n can't do that!",name,"doesn't exit in pair")
    elif choice == "4":
        name = input("Enter the name of the person you want to replace: ")
        dad_name = input ("Enter new dad's name:")
        if name in pair:
            pair[name] = dad_name
        else:
            print("The Person name doesn't exit, try adding it")
    else:
        print("\nSorry, but", choice,"isn't a valid choice")

input("\n\nPress the enter key to exit")
                  

            
    
            
    
