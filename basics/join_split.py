stats = {
    "Strength",
    "Constitution",
    "Dexterity",
    "Intelligence",
    "Wisdom",
    "Charisma",
}

for stat in stats:
    print(stat)

separator = " | "
output = separator.join(stats)
print(output)

# -------------------------------------
sentence = "The quick red fox jumped over the fence"

words = sentence.split()
print(words)

numbers = "9,456,845,852,213,021"
print(numbers.split(","))

# -------------------------------------

generate_list = ["9"," ",
          "4", "5", "6", " ",
          "8", "4", "5", " ",
          "8", "5", "2", " ",
          "2", "1", "3", " ",
          "0", "2", "1", " ",]
values = "".join(generate_list).split()
print(values)

# replace values
for i in range(len(values)):
    values[i] = int(values[i])

print(values)

# create new list
int_values = []
for value in values:
    int_values.append(int(value))

print(int_values)
