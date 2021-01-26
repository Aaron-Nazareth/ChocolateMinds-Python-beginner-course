# 1. Print the individual characters of a string "hello" using for loop.

message = "Hello"

for characters in message:
    print(characters)

# 2. Print the individual characters of a string "hello" using for loop but all the letters must be printed as capitals.

message = "Hello"

for characters in message:
    print(characters.upper())

# 3. Prompt the user to provide his/her name, print each of the letters using for loop, all lower case.

name = input("What is your name? ")

for characters in name:
    print(characters.lower())

# 4. Print this sentence "i love python", capitalizing the first letter of each word.

sentence = "i love python"
print(sentence.title())

# 5. Print the individual letters from this sentence "i love python" using for loop, make sure first letter of each word
# is capitalized.

sentence = "i love python"

for characters in sentence.title():
    print(characters)

# 6. Create a list of your favourite friends, make sure you have at least 5 of them in that list. Using "for" loop,
# print them one by one with a message "Hello, how are you {friend_name}".

favourite_friends = ["Liam", "Ryan", "Joanna", "Finian", "Brandon"]

for names in favourite_friends:
    print(f"Hello, how are you {names}")

# 7. Create a list of roll numbers from 1 to 25 using range function. Create a for loop printing each of them with a
# message "Roll number {number}"

roll_numbers = range(1,26)

for numbers in roll_numbers:
    print(f"Roll number {numbers}")

# 8. An ATM dispenses £5, £10, £20, £50 notes. Create a program using a for loop dispensing the note. When dispensing
# each of these notes, make sure you print a message to the user saying "Here's your {denomination}"

atm_money_denominations = [5, 10, 20, 50]

for denominations in atm_money_denominations:
    print(f"Here's your £{denominations}")

# 9. A circus charges different ticket prices depending on a person’s age. The ticket is free for a person under the
# age of 10, if they are between 11 and 16, the ticket is £5; and if they are above age 16, the ticket is £10. Write
# a program asking their age. Calculate the cost of the ticket and tell them how much it'll cost them.

age = int(input("What is your age? "))

if age <= 10:
    print("Your ticket is free")
elif 11 <= age <= 16:
    print("Your ticket will cost £5")
else:
    print("Your ticket will cost £10")