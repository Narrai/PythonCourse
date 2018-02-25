fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("*" * 40)
# ordered_keys = list(fruit.keys())  # return all the keys
# ordered_keys.sort()  # sort the keys
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + ": " + fruit[f])

# ANOTHER WAY
# for f in sorted(fruit.keys()):
#     print(f + ": " + fruit[f])

# # print only values
# for val in fruit.values():
#     print(val)
#
# print("*" * 50)
# # ANOTHER WAY
# for key in fruit:
#     print(fruit[key])

# print(fruit.keys())
# print("-" * 50)
# print(fruit.values())


fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

print(fruit.items())

