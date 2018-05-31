# Exclusive Network
# Demostrates logical operator ans compound condition

print("\tExclusive Computer Network")
print("\t\tmembers only!\n")

security = 0

username = ""
while not username:
    username = input("username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "Abdulvahab" and password == "Fatema!786":
    print("Hi. Abdulvahab.")
    security = 5
elif username == "Musu" and password == "Khushi1786":
    print("Hi. Musu.")
    Security = 3
elif username == "Fatema" and password == "Fatema1786":
    print("How goes it, will?")
    security = 3
elif username == "guest" or password == "guest" :
    print("Welcome, guest.")
    security = 1
else:
    print("login failed. You are not so exclusive.\n")

input("\n\nPress the enter key to exit")
