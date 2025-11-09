import random
print(random.randint(0, 1))
player = "x"
computer = "o"

def startGame():
  global player, computer
  player = input("Do you want to be 'x' or 'o'?")
  if(player == 'o'):
    computer ='x'

startGame()
print(player)
print(computer)

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

weather_data = threeday_weather_report(weather_data)
print(weather_data[0])
print(weather_data[1])
print(weather_data[2])
