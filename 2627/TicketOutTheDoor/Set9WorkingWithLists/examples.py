store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line) 


houses = []
houses += ["Wilma", "Barney", "Homer", "Marvin"]
print(houses)
houses.insert(0, houses.pop())
print(houses)


# cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

# removed_element = cs_topics.pop()
# print(cs_topics)
# print(removed_element)

# cs_topics.pop(4)
# print(cs_topics)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


my_range3 = range(1, 100, 10)
print(list(my_range3))

letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
first_three = fruits[:3]
print(first_three)

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i)

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs)

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names)
print(names)

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse = True)
print(sorted_cities)


games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)