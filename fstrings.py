# f-strings -> formatted strings

name = "Aaron"
age = 22
print(f"Hello, {name}. You are {age} years old.")

# program to fetch a hobby from the user and print out using fstring

hobby = input("What is your favourite hobby? ")
print(f"Your favourite hobby is {hobby}")

# Ask for user's fav movie and fav snack. Print using the same format string with two variables.

fav_movie = input("What is your favourite movie? ")
fav_snack = input("What is your favourite snack? ")
message = "Hello your favourite movie is {0} and favourite snack is {1}".format(fav_movie, fav_snack)
print(message)
