# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# key_to_check = "Landmark 81"

# print(building_heights.get('Shanghai Tower', 0)) # Prints 632
# print(building_heights.get('Mt Olympus', 0)) # Prints 0
# print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'

# survey_responses = [
#     {"age": 25, "income": 50000, "city": "Seattle"},
#     {"age": 32, "income": 62000},                  # missing city
#     {"age": 45, "city": "Chicago"},                 # missing income
#     {"age": 29, "income": 54000, "city": "Austin"}
# ]

# for s in survey_responses:
#     city = s.get("city", "Unknown")
#     print(city)





# count = 0
# total_income = 0
# for entry in survey_responses:
#     if(entry.get('income') != None):
#         total_income += entry.get('income')
#         count += 1

# avg_income = total_income/count
# print(avg_income)

# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(320291, "No Prize"))
# # Prints "Gift Basket"
# print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(100000, "No Prize"))
# # Prints "No Prize"
# print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(872921, "No Prize"))
# # Prints "Concert Tickets"
# print(raffle)
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# for student in test_scores.keys():
#  print(student)

# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# # print(test_scores.values())



# for score_list in test_scores.values():
#  print(score_list)




# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# for company, value in biggest_brands.items():
#  print(company + " has a value of " + str(value) + " billion dollars. ")


# tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

# spread = {}
# spread["past"] = tarot.pop(13)
# spread["present"] = tarot.pop(22)
# spread["future"] = tarot.pop(10)

# for key, value in spread.items():
#   result = "Your {key} is the {value} card".format(key = key, value = value)
#   print(result)


# survey_response = {
#     "age": 34,
#     "income": 72000,
#     "education": "Bachelor's",
#     "city": "Denver"
# }
# column_names = survey_response.keys()


# for c in column_names:
#       print(c)

# expected_fields = ["age", "income", "education", "city", "state"]

# missing_fields = []
# for f in expected_fields:
#     if(f not in survey_response.keys()):
#         missing_fields.append(f)
        
# print(missing_fields)

# exercise_data = {
#     "Alice": 5,
#     "Bob": 3,
#     "Charlie": 7,
#     "Diana": 4
# }

# total = 0

# for value in exercise_data.values():
#     total += value
# avg = total/len(exercise_data)
# print(avg)

pct_women = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for k,v in pct_women.items():
    result = "Women make up {percent} percent of {profession}s".format(percent = v, profession = k)
    print(result)