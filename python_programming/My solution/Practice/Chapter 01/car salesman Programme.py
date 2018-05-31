# Car salesman Programme
# Calculates actual value of the car including taxes and services
name = input("what's your good name Mr/Miss:")
car_make = input("which car do you like: ")
model = input("good, and model:")
miles = float(input("how many miles is your home? :"))


base_value = float(input("ok. Base value of this car is $"))
tax = 0.2*base_value
licence = 0.05*base_value
dealer_prep = 500
des_charge = 2*miles           
actual_value = base_value+ tax+ licence+ dealer_prep+ des_charge

print("this fantastic car will cost you only $",actual_value,\
      "at your door step\n"+"what do you think? Mr", name)
