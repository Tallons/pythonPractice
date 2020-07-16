data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[16:]   # this wont work because you deleted [0:2] on line 4. use [14:]
# print(data)

min_valid = 100
max_valid = 200

# incorrect way
#     for index, value in enumerate(data):
#         if (value < min_valid or value > max_valid):
#             del data[index]
#                 # cant use index -= 1 in python
#
#     print(data)


# remove low values
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]
print(data)

# remove high values
start = 0
# 2nd -1 is the start value (start at end) 3rd -1 is to loop backwards
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

del data[start:]
print(data)


#  ------------------------------------------------------

data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102]

min_valid = 100
max_valid = 200

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data, data[index])
#         del (data[index])

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del (data[top_index - index])


print(data)