# FizzBuzz

# multiple of 3 -> say Fizz
# multiple of 5 -> say Buzz
# multiple of both 3 and 5 -> say FizzBuzz
# if multiple of neither -> state number normally

for number in range(1, 16):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
