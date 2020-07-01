t = "a", "b", "c" # or ("a", "b", "c")
print(t)

print("a", "b", "c") # this is not a tuple
print(("a", "b", "c"))


color = "blue", "red", "orange", "yellow"

# color[1] = "purple"
# line 10 with cause an error - tuples are immutable
# you can reassign as shown on line 14

color = color[0], "purple", color[2], color[3]
print(color)


