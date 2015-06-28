# Define the total number of cars in the fleet.

cars = 100

# Define how many people can fit in a car

space_in_a_car = 4.0

# Define the number of available drivers today

drivers = 30

# Define the number of passengers

passengers = 90

# Define the number of cars not driven by subtracting the number of drivers
# available from the numbrer of cars available.

cars_not_driven = cars - drivers

# Define the number of cars that will be driven as the same as the number of 
# Drivers for the day.

cars_driven = drivers

# Define the number of people that can be accomodated in the carpool as the 
# prodcut of the number of cars driven multiplied by the space in a car.

carpool_capacity = cars_driven * space_in_a_car

# Define the average number of people in a car given the number of cars on 
# the road by dividing the number of passengers by the number of cars driven.

average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaliable."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills
# ------------
# 1. the use of 4.0 is arbitrary here because all math is with whole numbers.  
# Changing it to 4 makes no difference in this program.
# 2. It's true that 4.0 is a floating point number
# 3. This file includes the comments
# 4. "=" is used for assignment, where as "==" is used for mathmatical equality.
# 5. Yes, I'm familiar with the underscore - it is used in place of spaces in 
# unix_and_programing
