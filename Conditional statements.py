# 1. Any student who scores above 50 marks in an exam is given a pass. Can you write a conditional "if" statement
# checking the mark is above 50? If the mark is above 50, simply write "You are a star!" to the console.

student_mark = int(input("What is your mark? "))
if student_mark > 50:
    print("You are a star!")
else:
    print("Unfortunately, you have failed the exam")

# 2. The school realised that the pass grade needs to be changed to "greater than or equal to" 50 is a pass. Can you
# update your if statement with this new boolean conditon?

student_mark = int(input("What is your mark? "))
if student_mark >= 50:
    print("You are a star!")
else:
    print("Unfortunately, you have failed the exam")


# 3. The school want to update their pass criteria. The new criteria is that if the mark is over 60 it's a pass or
# it's a fail. Can you write a if-else condition to printing out "You are a Star" if passed or "Well, you shouldn't be
# playing Fortnite :)" if failed.

student_mark = int(input("What is your mark? "))
if student_mark > 60:
    print("You are a star!")
else:
    print("Well, you shouldn't be playing Fortnite :)")

# 4. In addition to pass grade, the school created a new grade called distinction. If a student scores 80 or above 80,
# student will be awarded distinction. If the student scores above 60, the student will be awarded pass. Can you
# write an if statement for both these conditions

student_mark = int(input("What is your mark? "))
if student_mark >= 80:
    print("Congratulations, you have achieved a distinction!")
elif 60 < student_mark < 80:
    print("Congratulations, you have passed!")
else:
    print("Unfortunately, you have failed")
