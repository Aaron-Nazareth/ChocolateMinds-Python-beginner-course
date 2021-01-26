# 1. Create a program with one variable for representing a country. Ask the user the capital city of this country.
# Capture the user's response and print out to the console something along the lines of this: "The capital city of {
# country} is {user_response}

country = "England"
user_response = input(f"What is the capital of {country}? ")
print(f"The capital city of {country} is {user_response}")

# 2. Create a program with one variable representing the temperature in Fahrenheit. Convert the temp in F to Celcius.
# Print both Fahrenheit and Celcius temperatures

temperature_fahrenheit = 89.6
temperature_celsius = (float(temperature_fahrenheit)-32)*(5/9)
print(f"The temperature in Fahrenheit is {temperature_fahrenheit} and the temperature in Celsius is {temperature_celsius}")

# 3. Re-create the same problem mentioned in #2 except this time ask the user to input the Fahrenheit. For example,
# "Hello, please enter the current temp in Fahrenheit".  Convert the temp in F to Celcius. Print both Fahrenheit and
# Celcius temperatures as f-string like : "Temperature of {f} is {c}"

temperature_fahrenheit = input("What is the current temperature in Fahrenheit? ")
temperature_celsius = (float(temperature_fahrenheit)-32)*(5/9)
print(f"Temperature of {temperature_fahrenheit} Fahrenheit is equivalent to {temperature_celsius} Celsius")

# 4. Create a program asking the user to enter the temperature in Celcius. This time convert the temperature into
# Fahrenheit and output the values of both temperatures using f-strings like : "Temperature of {f} is {c}".

temperature_celsius = input("What is the current temperature in Celsius? ")
temperature_fahrenheit = (float(temperature_celsius)*(9/5)+32)
print(f"Temperature of {temperature_celsius} Celsius is equivalent to {temperature_fahrenheit} Fahrenheit")

