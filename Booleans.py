# 1. Print the output from the following statement.

# python = "I love Python. My mon hates Python and probably get a heart attack if she sees one. My dad kills a Python if he sees one"
#
# python_type = bool(python)
# print(python_type)

# 3. It seems tomorrow is not a sunny day according the Dimpy the weather forecaster. But your job is to ask her the
# weather for tomorrow. Write a program asking Dimpy what is the weather like tomorrow. Use input to capture the
# input from Dimpy. Note Dimpy will answer in one of the phrases only: "sunny", "cloudy", "rainy", "snowy" Based on
# her answer, can you write an "if" statement to let your family know if the family can go out if it's sunny,
# or stay put if any of the other weather forecast?

weather_tomorrow = input("What is the weather tomorrow? ")
if weather_tomorrow == "sunny":
    print("Family may go out")
elif weather_tomorrow == "cloudy":
    print("Family must stay put")
elif weather_tomorrow == "rainy":
    print("Family must stay put")
elif weather_tomorrow == "snowy":
    print("Family must stay put")
else:
    print("Invalid input")