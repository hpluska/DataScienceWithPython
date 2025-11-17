import requests 
import csv
import pandas

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_002E&for=state:*') 
r_json = r.json()#converts the data into a usable Python data structure

# writes the data to a filel called census.csv
with open('census.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r_json)

census_df = pandas.read_csv("census.csv")
print(census_df.head())