# Finicky Counter
# Demostrates the break and continue statement

count = 0
while True:
    count += 1
# End loop while count greater than 10
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

input("\n\nPress the enter key to exit.")
