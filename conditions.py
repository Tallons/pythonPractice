age = 25

if 16 <= age <= 65:
    print("Have a good day at work")

if age < 16 or age > 65:
    print("Enjoy your free time")

day = "Monday"
temperature = 85
raining = True

if day == "Saturday" and temperature > 70 and not raining:
    print("Go swimming")
else:
    print("Learn Python")


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