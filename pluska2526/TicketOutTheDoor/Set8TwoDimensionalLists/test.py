# names = ["Noelle", "Ava", "Sam", "Mia"]
# heights = [61, 70, 67, 64]

# print(names[0], "is", heights[0], "inches tall")
# print(names[1], "is", heights[1], "inches tall")
# print(names[2], "is", heights[2], "inches tall")
# print(names[3], "is", heights[3], "inches tall")

# heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]+ [["Vik", 68]]

# print(heights)


# #A 2d list with three lists in each of the indices. 
# tic_tac_toe = [
#             ["X","O","X"], 
#             ["O","X","O"], 
#             ["O","O","X"]
# ]

# #Access the sublist at index 0, and then access the 1st index of that sublist. 
# noelles_height = heights[0][1] 
# print(noelles_height)

# grade_book = [
#     [5, 4.5, 3, 4, 3,5],
#     [2, 3, 2.5, 4, "R"], 
#     [4, 1, 3.5, 5, 4], 
#     [5, 2, 3.5, 3, 4.5]
#     ]

# result = grade_book[1][4]
# print(result)

# class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
# class_name_hobbies[-1][-1] = "Football"
# print("Negative indices example: " + class_name_hobbies[-1][-1])

# names = ["Jenny", "Alexus", "Sam", "Grace"]
# heights = [61, 70, 67, 64]
# names_and_heights = zip(names, heights)
# print(names_and_heights)

# converted_list = list(names_and_heights)
# print(converted_list)

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

owners_and_dogs_names = zip(owners, dogs_names)
list_of_names = list(owners_and_dogs_names)
print(list_of_names)
print(list_of_names[0][0])#you can print
list_of_names[0][0] = "new name"#but you cannot modify

print(list_of_names)

