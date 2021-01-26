# 1. The initial value of room temperature is 0 degrees. Write a program to print the temperature of the room for
# every degree increase. When the temerature reaches 24 degress, print the message "It's hot, shutting down" message
# and exits.

room_temperature = 0

while room_temperature < 24:
    print(f"The room temperature is {room_temperature} degrees celsius")
    room_temperature += 1

print("It's hot, shutting down")

# 2. A movie cinema sells 79 tickets per show. Print a message "Issued a ticket  {ticket_number} " for every
# purchase. When the show is full, print "House full, no more tickets available".

movie_tickets_sold = 0

while movie_tickets_sold <= 79:
    print(f"Issued ticket number {movie_tickets_sold}")
    movie_tickets_sold += 1

print("House full, no more tickets available")

# 3. Write a program to print integers from 0 till 100 using while loop. Make sure you use range function for
# fetching the integers.

integer = 0

while integer in range(0, 101):
    print(integer)
    integer += 1

# 4. A variable "visitor_counter" keeps a tracks of website visitors. The initial value of the counter is 0. Write a
# program using while loop to print out the visitor number for each time a visitor visits the site.  If the visitors
# are over 100, exit the while loop and print "System overloaded, exiting" message to the console.

visitor_number = 0

while visitor_number <= 100:
    print(f"Visitor number {visitor_number}")
    visitor_number += 1

print("System overloaded, exiting")

# 5. A receptionist chatbot at a dental practice asks for each of the patient's name as they enter the practice. The
# chatbot stops asking when it receives a "quit" word. Your job is to assist in writing a receptionist chatbot program.

patient_name = input("What is your name? ")

while patient_name != "quit":
    print(f"Your name is {patient_name}")
    patient_name = input("What is your name? ")

# 6. Write a loop that prompts the user to enter a series of numbers to guess a number game (guessing the number
# isn't the point of program here, remember). The loop ends once they say 0 value. Print out the the numbers as they
# guess. Print out "I give up" once the program receives 0 and exits.

number = input("Insert your number guess here: ")

while number != "0":
    print(number)
    number = input("Insert your number guess here: ")
print("I give up")
