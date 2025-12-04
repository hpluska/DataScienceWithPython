# pet = "Sparky the dog"

# letters = pet[len(pet)]
# print(letters)
favorite_fruit = "blueberry"
# print(favorite_fruit[:4])
# print (favorite_fruit[4:])
word = "flueberry"
word = "b" + word[1:]

print(word)
new_word = word[-1] + word[1:-1] + word[0]

print(new_word)

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

def common_letters(string_one, string_two):
  common = []
  for l in string_one:
    if(l in string_two and not l in common):
      common.append(l)
  return common

print(common_letters('manhattan', 'san francisco'))




