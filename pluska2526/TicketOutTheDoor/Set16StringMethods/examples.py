# featuring = "!!!Rob Thomas       !!!!!"
# print("'",featuring.strip('!'),"'")


# raw_line = "   California ,  large population ,  tech hubs   "
# raw_list = raw_line.split(",")
# # cleaned_list = [v.strip() for v in raw_list]
# cleaned_list = []
# for entry in raw_list:
#     cleaned_list.append(entry.strip())
# cleaned_line = "|".join(cleaned_list)
# print(cleaned_line)


raw_income = ["$45,000", "$82,300", "$9,500"]
clean_income = []

for value in raw_income:
       temp = value.replace("$", "")
       temp2 = temp.replace(",","")
       clean_income.append(int(temp2))
print(clean_income)

# for value in raw_income:
#     # remove $ and , characters
#     number = value.replace("$", "").replace(",", "")
#     clean_income.append(int(number))

# print(clean_income)

# log_line = "[INFO] user_id=42, load_time=351ms, status=OK"
# load_time = log_line.find("load_time=")
# time_end = log_line.find(",", load_time)
# time_start = load_time + len("load_time=")
# time_ms = log_line[time_start:time_end]
# time = int(time_ms.strip("ms"))
# print(time)


# def state_summary(state, population, income):
#     result = "State: {state}\n"
#     result += "Income: ${income}\n"
#     result += "Population: {population}"
#     return result.format(state = state, income = income, population = population)

# summary = state_summary("California", 39500000, 84000)
# print(summary)

# info = "Alice, Seattle, WA 98108"
# data = info.split(",")
# state_zip = data[2].split()
# name = data[0]
# city = data[1]
# state = state_zip[0]
# zip = state_zip[1]

# print(name, city, state, zip)

# spring_storm_text = """The sky has given over  
# its bitterness.  
# Out of the dark change  
# all day long  rain falls and falls 
# as if it would never end.  
# Still the snow keeps  
# its hold on the ground.  
# But water, water  
# from a thousand runnels!  
# It collects swiftly,  
# dappled with black  
# cuts a way for itself  
# through green ice in the gutters.  
# Drop after drop it falls  
# from the withered grass-stems  
# of the overhanging embankment.""" 

# text = spring_storm_text.split("\n")
# print(text)

# total = 0
# for line in text:
#     total += len(line)

# avg = total/len(text)
# print(avg)

fields = ["California", "39500000", "84000", "45000"] 

fields_text = ",".join(fields)
print(fields_text)


fields_text = "\t".join(fields)
print(fields_text)