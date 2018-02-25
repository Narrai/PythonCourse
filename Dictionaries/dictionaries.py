"""Dictionaries are unordered sequences and cannot contain duplicate
items in and index is meaningless, but contain key-value pair and key is the
best means to accessed the value"""

fruit = {"orange": "a sweet, orange, citrus fruit",
         "lemon": "good for making cider",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# print(fruit["lemon"])

# adding another fruit to the dictionary
# if we assign value to an existing key, it results in replacing value rather than adding the value to it
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# fruit["pear"] = "great with tequila"
# print(fruit)

# del method remove the item from the dictionary
# del fruit["lime"]

# If key is forgot to use with del, then entire dictionary will be deleted
# del fruit

# If you want to clear only the contain not the dictionary object as a whole
# fruit.clear()
print(fruit)

# while True:
#     dict_key = input("Please enter fruit name: ")
#     if dict_key == "quit":
#         break
#     # description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # print(description)
#     if dict_key in fruit:  # this replaced the has_key in python 3
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)

# to print all the from fruit
for snack in fruit:
    print(fruit[snack])
