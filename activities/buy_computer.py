# current_choice = "-"
# computer_parts = []
#
# while current_choice != "0":
#     if current_choice in "12345":
#         print("Adding {}".format(current_choice))
#         computer_parts.append(current_choice)
#     else:
#         print("Please select what you are looking for:")
#         print("1: Computer")
#         print("2: Monitor")
#         print("3: Mouse")
#         print("4: Keyboard")
#         print("5: Speakers")
#         print("0: Finished shopping")
#     current_choice = input()
#
# print(computer_parts)

available_parts = ["Computer", "Monitor", "Mouse", "Keyboard", "Speakers", "HDMI Cable"]
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please select what you are looking for:")
        for index, part in enumerate(available_parts):
            print("{0}: {1}".format(index + 1, part))

    current_choice = input()

print(computer_parts)