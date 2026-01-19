import pandas as pd

# my_dictionary = {
#     'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
#     'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
#     'age': [34, 28, 51]
# }

# my_df = pd.DataFrame(my_dictionary)

# my_list = [
#     ['John Smith', '123 Main St.', 34],
#     ['Jane Doe', '456 Maple Ave.', 28],
#     ['Joe Schmo', '789 Broadway', 51]
#     ]

# fields=['name', 'address', 'age']

# my_df2 = pd.DataFrame(my_list, columns = fields)

# print(my_df2)

# cakes = pd.read_csv('csv_data.csv')
# print(cakes["topping"])
# print(cakes.topping)


df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

result = df[df['month'].isin(['March','May'])]
print(result)

# print(df['clinic_north'])

# row_2 = df.iloc[2]
# print(row_2)

# orders.iloc[3:7]


# df = pd.DataFrame([
#   ['Martha Jones', '123 Main St', '234-567-8910', 28],
#   ['Rose Tyler', '456 Maple Ave.', '212-867-5309', 22],
#   ['Donna Noble','789 Broadway', '949-123-4567', 35],
#   ['Amy Pond','98 West End Ave.', '208-580-8760', 31],
#   ['Clara Oswald','54 Columbus Ave.', '714-225-1957', 33]
#   ],
#   columns=['name', 'address','phone', 'age']
# )

# results = df[df.name.isin(['Martha Jones',
#      'Rose Tyler',
#      'Amy Pond'])]

# results.reset_index(drop = True, inplace = True)
# print(results)


