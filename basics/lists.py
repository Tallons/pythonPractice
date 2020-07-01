weapon_list = ["sword", "axe", "polearm", "flail"]

weapon_list.append("mace")

for state in weapon_list:
    print("This weapon is a " + state)

# -----------------------------------------

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort() # not a new object
print(numbers)
# print(sorted(numbers)) - this is a new object

# -----------------------------------------

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print ("The lists are equal")

print(list("The lists are equal"))

# -----------------------------------------

my_list = ["monday", "tuesday", "wednesday", "thursday", "friday",
           "saturday", "sunday"]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

for i in my_list:
    print(i)

# -----------------------------------------

my_list = list(range(10))
print(my_list)

even = list(range(0, 11, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)
print(even[3]) # [0, 2, 4, 6, 8, 10] = 6

# -----------------------------------------

color = ["blue", "red", "orange", "yellow"]
print(color)
color[0] = "purple"
print(color)