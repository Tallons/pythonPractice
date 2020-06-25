import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))


while guess != answer:
    guess = int(input())

    if guess == answer:
        print("You Win!")
    else:
        if guess < answer:
            print("Please guess higher, try again")
        else:
            print("Please guess lower, try again")