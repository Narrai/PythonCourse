"""pickle module saves data in memory whereas shelve module stores data
in files. Like dictionary shelve work as key value pair and values can be
anything that can pickle. keys are string, but immutable objects like tuples.
All methods that can be used with dictionary can be used with shelve and act as
persistence dictionary. Like pickle, shelve files are also risk with untrusted sources.
shelve keys must be string but dictionary keys can any immutable objects"""

import shelve

# with shelve.open("ShelfTest") as fruit:
fruit = shelve.open("ShelfTest")
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making soda"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# UPDATE THE VALUE
# fruit['lime'] = "great with tequila"

# Loop and print the key and corresponding value
# for key in fruit:
#     print(key + ": " + fruit[key])

# print(fruit)

# get method to retrieve value
# while True:
#     shelve_key = input("Please enter a fruit: ")
#     if shelve_key == "quit":
#         break
#     # description = fruit.get(shelve_key)  # return none if key does not match
#     description = fruit.get(shelve_key, "We don't have a " + shelve_key)
#     print(description)

# By using in key
# while True:
#     fruit_key = input("Please enter a fruit: ")
#     if fruit_key == "quit":
#         break
#     if fruit_key in fruit:
#         description = fruit[fruit_key]
#         print(description)
#     else:
#         print("We don't have " + fruit_key)

# Printing order keys in fruit
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for key in ordered_keys:
#     print(key + "-" + fruit[key])

# printing values, items of shelve
for v in fruit.values():
    print(v)
print(fruit.values())

print("*" * 40)

for item in fruit.items():
    print(item)
print(fruit.items())

fruit.close()
# with shelve.open("ShelfTest") as fruit:
#     fruit = {'orange': "a sweet, orange, citrus fruit",
#              'apple': "good for making soda",
#              'lemon': "a sour, yellow citrus fruit",
#              'grape': "a small, sweet fruit growing in bunches",
#              'lime': "a sour, green citrus fruit"}
#     print(fruit["lemon"])
#     print(fruit["grape"])
# print(fruit)
