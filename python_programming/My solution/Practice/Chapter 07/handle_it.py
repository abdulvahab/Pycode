# handle_it
#
# Demostrates handling exception
#
# try/except
try:
    num = float(input("Enter a number: "))

except:
    print("something went wrong!")

# specifying exception type

try:
    num= float(input("\nEnter a number:"))
except ValueError:
    print("That was not a number!")

# Handling multiple exception types

print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value,"-->", end="")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")
print()
for value in (None,"Hi!"):
    try:
        print("Attempting to convert", value,"-->", end="")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")

# get the exception's argument
    try:
        num = float(input("\nEnter a number:"))
    except ValueError as e :
        print("That was not a number! or as Python would say....")
        print(e)
# try/except/else
try:
    num = float(input("\nEnter a number:"))
except ValueError:
    print("That was not a number!")
else:
    print("you entered the number", num)

input("\n\nPress the Enter key to exit:")
               
