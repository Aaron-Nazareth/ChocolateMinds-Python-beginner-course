# 1. Write a function which has the following requirements:
#  - takes in name of the person;
#  - expects a four or more characteristics about him/her

def person_characteristics(name, *characteristics):
    print(f"Hello {name}, you have the following characteristics: {characteristics}")

person_characteristics("Steven Gerrard", "leader", "great finisher", "great vision", "driven")

# 2. Write a function that iterates through list of animals using the same logic as the example given for this question.

def pets(animals):
    for animal in animals:
        print(animal)

animals = ["dog", "cat", "hamster", "parrot"]
pets(animals)

# 3. Write a function that calculates the area of a rectangle given len and width.
# Call it with 12, 13 as len and width.

def rectangle_area(len, width):
    area = len * width
    return area

print(rectangle_area(12, 13))

# 4. Whenever I call the example function for this question, an addition of "Chairs" should be amended. Can you work
# on this requirement?

def furniture(items):
    items.append("Chairs")
    return items

items = ["Table","Basket","Lamp"]
print(furniture(items))
