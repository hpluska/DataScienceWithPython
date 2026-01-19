

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
print(students)
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}


def update_stats(dict, stats, value):
    dict[stats] = value
    return dict

result = update_stats(menu, "oatmeal", 10)
print(result)


cities = ["NYC", "LA", "Chicago", "Houston"]
avg_temps = [70, 75, 65, 80]

city_temps = {cities:avg_temps for cities, avg_temps in zip(cities, avg_temps)}

print(city_temps)

