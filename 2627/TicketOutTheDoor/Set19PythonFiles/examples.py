# with open("some_lines.txt") as lines_doc:
#   all_lines = lines_doc.readlines()
#   for line in all_lines:
#     print(line)

# with open("some_lines.txt") as lines_doc:
#   lines_doc.readline() 
#   lines_doc.readline() 
#   lines_doc.readline() 
#   print(lines_doc.readline())


with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("Twisted Sister")

# with open('bad_bands.txt', 'a') as bad_bands_doc:
#   bad_bands_doc.write("\nMotley Crew")
#   bad_bands_doc.write("\nRATT")

# with open('users.csv') as log_csv_file:
#   print(log_csv_file.read())

# import csv

# user_emails = []
# with open('users.csv', newline='') as users_file:
#   user_dict = csv.DictReader(users_file)  #turns the users_file into rows of dictionaries
#   for row in user_dict:
#     user_emails.append(row["Email"])

# print(user_emails)


# with open('addresses.csv', newline = "") as user_addresses:
#   address_dict = csv.DictReader(user_addresses, delimiter = ";")
#   for row in address_dict:
#     print(row)


# import csv
# with open("books.csv") as books_file:
#   books_dict = csv.DictReader(books_file, delimiter = "@")
#   isbn_list = []
#   for book in books_dict:
#     isbn_list.append(book["ISBN"])
#   print(isbn_list)

# import csv
# access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}] 
  

# with open("logger.csv", "w") as logger_csv:
#   fields = ['time', 'limit', 'address'] 
#   log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
#   log_writer.writeheader()
#   for log in access_log:
#     log_writer.writerow(log)

# import json 
# with open('message.json') as message_json: 
#   message = json.load(message_json) 
#   print(message[0]["text"])