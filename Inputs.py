# 1. Write a program asking for user's name and store the user's name in a variable. Print the greeting "Hello,
# <user_name>"

name = input("What is your name? ")
print("Hello, "+name)

# 2. Write a program asking user's name and age. Print out the message "Hello <user_name>, you are <aga> old" message
# as your output

age = input("What is your age? ")
print("Hello "+name+", you are "+age+" years old")

print(type(age))

age = int(age)
print(type(age))

