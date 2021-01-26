# friends = open("Names", "r")
# print(friends.read())

# print(friends.readline())
# print(friends.readline())
# print(friends.readline())

# count = 1
# for name in friends:
#     print(count)
#     count += 1
#     print(name)

animals = open("Animals", "r")

for animal in animals:
    print(animal)

animals.close()
