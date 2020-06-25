parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot.casefold():
    print("{} is in {}".format(letter, parrot))
else:
    print("letter not found")

activity = input("What would you like to do today?")

if "movie theatre" not in activity.casefold():
    print("But I want to go to the movie theatre")