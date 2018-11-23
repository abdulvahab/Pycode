#!/usr/bin/env python
# find averaage of function in given integer array.
numbers = []
choice = 'y'
while choice == 'y':
    n = int(input("Please Enter your number: "))
    choice = input("would you like to add more numbers (y/n) ?")
    numbers.append(n)
length = len(numbers)
sum = 0
for n in numbers:
    sum += n
print("Average: ", sum/length)

def average(*numbers):
    sum = 0
    length = len(numbers)
    for n in numbers:
        sum += n
    print("Average: ", sum/length)
average(1,2,3)
