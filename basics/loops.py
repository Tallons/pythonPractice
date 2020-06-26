# ****** FOR LOOPS ******
school = "DevMountain"

for character in school:
    print(character)

# ---------------------------------

number = input("please enter a series of number with any kind of seperator (ex. , / < ; letters etc.) ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators += char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

# --------------------------------------------------

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capital_letters = ""

for char in quote:

    if char != char.lower():
        capital_letters += char

print(capital_letters)

# --------------------------------------------------

for i in range(10):
    print(i)

# --------------------------------------------------

for i in range(10, 0, -2):
    print(i)


# ****** WHILE LOOPS ******


i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

# --------------------------------------------------
available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

else:
    print("you an found exit")

# --------------------------------------------------

choice = "-"

while choice != "0":

    if choice in "12345":
        print("You have selected {}".format(choice))
    else:
        print("Please choose your option from the list below: ")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to bed")
        print("0.\tExit")

    choice = input()

