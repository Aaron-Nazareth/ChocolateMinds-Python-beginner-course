# 1. Define a function "greet". It takes no parameters. But it will print out a message "Good morning, how do you
# do?" everytime you call it.
# Once you define it, can you call it couple of times?

def greet():
    print("Good morning, how do you do?")

greet()
greet()

# 2. Define a function that takes in a name parameter. Based on the received name as the input to the function,
# it will print the message "How are you, ___<name>____?" Call with your name, your mum's name, your friend's name
# and your dad's name. Also call without any name. Explain what happens if there's no name provided.

def greet(name):
    print(f"Hello, how are you {name}?")

greet("Aaron")
greet("Mum")
greet("Mike")
greet("Dad")
greet() # call without name fails as argument is expected due to given function parameter

# 3. Define a function that accepts two parameters first_name and last_name. It then prints the full name as
# first_name  last_name.
# Call this function with your first name and last name. Make sure the names are separated with a space in between.

def full_name(first_name, last_name):
    print(f"{first_name} {last_name}")

full_name("Aaron","Nazareth")

# 4. Create a function that calculates the area of a circle given a radius. Define a local variable as pi = 3.14.
# Call the function with 10 cm, 12.5cm and 22.8cm.

import math
def circle_area(radius):
    area = math.pi * (radius **2) # could use "area = int(math.pi * (radius **2))" for rounded area values
    return area

print(circle_area(10))
print(circle_area(12.5))
print(circle_area(22.8))

# 5. Write a function to ask for a quote and print it; and call that function with a random quote
# For example, quote: "Knowledge is power" or "Dogs are not just for Christmas!"

def quote(user_quote):
    user_quote = input("Enter your message here: ")
    print(user_quote)

quote("Random quote")