pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram, key=str.casefold)
print(letters)

# -------------------------------------------

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]

sorted_numbers = sorted(numbers) # creates a sorted copy
print(sorted_numbers)

numbers.sort()    # sorts without copy - sort doesnt return a value (cant set to variable)
print(numbers)


# -------------------------------------------

names = ['Graham', 'teri', 'Maggie', 'john', 'Angi']
names.sort(key=str.casefold)
print(names)