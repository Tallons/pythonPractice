age = 25

if 16 <= age <= 65:
    print("Have a good day at work")

if age < 16 or age > 65:
    print("Enjoy your free time")

# --------------------------------------------------

day = "Monday"
temperature = 85
raining = True

if day == "Saturday" and temperature > 70 and not raining:
    print("Go swimming")
else:
    print("Learn Python")

# --------------------------------------------------

answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher, try again")
    else:
        print("Please guess lower, try again")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("You lose")
else:
    print("You win")

# --------------------------------------------------

name = input("Please enter guest's name: ")
age = int(input("Please enter guest's age: "))

if 18 <= age <= 31:
    # if age in range (18, 32):
    print("We will be awaiting your arrival")
else:
    print("I am sorry, this party is only for young adults")