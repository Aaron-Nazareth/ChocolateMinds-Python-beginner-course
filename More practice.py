# 1. Write a loop using "while" loop asking user for a random name. Quit the program if the random string is "q" or
# "quit" or "end" or "bye" or empty string. Also make sure the input can be of any case (user can input Q or q or
# Quit or qUiT - so make sure your program takes care of it.

name = input("What is your name? ").lower()

while name:
    if name == "q" or name == "quit" or name == "end" or name == "bye" or name == "":
        break
    else:
        print(name)
    name = input("What is your name? ").lower()

# 2. Create a program that reads the individual characters of a single-word string. If any of the character is "q"
# the program must quit. For example, "hello" will print all the characters but "queen" will not run.

word = input("Insert word here: ")

for characters in word:
    if characters.lower() == "q":
        exit()
    else:
        print(characters)

# 3. Write a for loop printing even numbers from 1 to 10 using "range" function

for numbers in range(1,11):
    if numbers % 2 == 0:
        print(numbers)

# 4. Using a for loop, can you write a program to print values 5, 4, 3, 2, 1, 0.

countdown = [5, 4, 3, 2, 1, 0]

for numbers in countdown:
    print(numbers)

# bonus alternative solution
print("Counting down...")
for numbers in countdown:
    if numbers == 0:
        print(f"{numbers}!")
    else:
        print(f"{numbers}...")

# 5. Prompt a user to provide his/her age. If the age is below 13, print out "You are pre-teen". If the age is equal
# to or above 13, print out "You are a teenager"

age = int(input("What is your age? "))

if age < 13:
    print("You are pre-teen")
elif 13 <= age < 18:
    print("You are a teenager")
else:
    print("You are an adult")
