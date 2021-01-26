# 1. Write a function that echo's what is given to it (single parameter).

def echo(parameter):
    print(parameter)
    print(parameter)

echo("Stop copying me")

# 2. Write a function that produces the square of the given number (single parameter).

def square_number(number):
    square = number **2
    return square

print(square_number(10))

# 3. Write a function that produces the square of the given number (single parameter). If the function is called
# without a number, it will return zero.

def square_number(number = 0):
    square = number **2
    return square

print(square_number())

# 4. Write a function that produces the cube of the given number.

def cubic_number(number):
    cube = number **3
    return cube

print(cubic_number(10))

# 5. Write a function that returns the multiplication of two given numbers. Call the function giving 10 and 20 as the
# numbers. Return the function with the result.

def multiplier(number1, number2):
    multiplication = number1 * number2
    return multiplication

print(multiplier(10, 20))

# 6. Write a function to calculate the area of a rectangle given the length and width. Return the value to the
# caller. Call the function with length = 192, width = 202.

def rectangle_area(length, width):
    area = length * width
    return area

print(rectangle_area(192, 202))
