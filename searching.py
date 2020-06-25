equipment_list = ["sword", "shield", "helm", "armor", "backpack", "bedroll"]

item_to_find = "armor"
found_at = None

# for i in range(len(equipment_list)):
#     if equipment_list[i] == item_to_find:
#         found_at = i

if item_to_find in equipment_list:
    found_at = equipment_list.index(item_to_find)
# the above code (lines 10-11) simplifies the code on lines 6-8

if found_at:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(found_at))
