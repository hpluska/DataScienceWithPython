def say_hello():
    print("Hello!")


def class_welcome(name1, name2):
  print("Welcome to Python!") 
  print("Get to work, " + name1)
  print(name2 + " sit!")


#class_welcome("Ayush", "Reid")

def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

# Using the default value of 10 for discount.
calculate_taxi_price(100, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(100, 0.5, 20)
