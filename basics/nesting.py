odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)


menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)

    else:
        print("{0} has a spam score: {1}".format(meal, meal.count("spam")))

 # Remove Spam (changes the list)
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

print("menu: ", menu)

 # Creates a new list without Spam
newMenu = []
for meal in menu:
    newMeal = []
    for item in meal:
        if item != "spam":
            newMeal.append(item)
    newMenu.append(newMeal)

print(newMenu, end="!")