print("Welcome to my python quiz :)")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who developed Python Programming Language? ")
if answer.lower() == "guido van rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Is Python case sensitive when dealing with identifiers? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("4 + 3 % 5? ")
if answer == "7":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" keyword used for function in Python language? ")
if answer.lower() == "def":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("character is used to give single-line comments in Python? ")
if answer == "#":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does pip stand for python? ")
if answer.lower() == "preferred installer programmer":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("truncation division operator in Python? ")
if answer == "//":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("eval is a keyword or not? ")
if answer.lower() == "no":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" arithmetic operator cannot be used with strings in Python? ")
if answer.lower() == "-":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
