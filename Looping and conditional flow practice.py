# 1. Write a program to check the temperature of a room. The requirements are simple: Prompt the user to enter the
# room temperature (it could be -100 to +100 including 0). Should the temperature of the room is below zero,
# shout out "It's freezing out here!". If the temperature is above zero, say "Ok, at least we aren't freezing". If
# the temperature is 0, say "Hmm, it's cold". If the user enters any number over 100 or below 100 degrees,
# alert him saying "I refuse to work with people who won't follow instructions:)"

room_temperature = int(input("What is the room temperature on a scale of -100 to +100 degrees? "))

if room_temperature < -100 or room_temperature > 100:
    print("I refuse to work with people who won't follow instructions")
elif room_temperature < 0:
    print("It's freezing out here!")
elif room_temperature > 0:
    print("Ok, at least we aren't freezing")
elif room_temperature == 0:
    # could also have else statement since all boundaries other than zero value are taken care of
    print("Hmm, it's cold")

# 2. Write a program to find out if the given number is a positive or negative or zero number.

number = int(input("Suggest a number for trial: "))

if number > 0:
    print("Positive value detected")
elif number < 0:
    print("Negative value detected")
else:
    print("Zero value detected")

# 3. Write a program to find out if the number is an even or odd number.

number = int(input("Suggest a number for trial: "))

if number % 2 == 0:
    print("Even number detected")
else:
    print("Odd number detected")

# 4. Given a range of numbers from 0 to 29,  write a program as per the requirements mentioned below:
# - if the number is a multiple of 3, print "Fizz"
# - if the number is a multiple of 5, print "Buzz"
# - if the number is a multiple of 3 and multiple of 5, print "FizzBuzz"
# - if the number is neither of the above, print the number

for number in range(0, 29):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 5. My mum sent me to Pizza Hut to pick up a pizza. There were quite a few toppings to select from. I was told to
# keep a note of these toppings so when she calls me I need to tell her.
#
# Write a program with a list of toppings. Make sure you have at least 10 toppings in your pizza (use your
# imagination). After noting down the toppings, I'll usually wait for my mum's call. When I receive her call I'll run
# through the toppings list shouting "Topping one is _______", "Topping two is ______".

available_toppings = ["Pepperoni", "Mince", "Ham", "Peppers", "BBQ chicken", "Tomatoes", "Onions", "Mushrooms",
                      "Olives", "Extra cheese"]

topping_number = 1

for toppings in available_toppings:
    print(f"Topping {topping_number} is {toppings}")
    topping_number += 1
