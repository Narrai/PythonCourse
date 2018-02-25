fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruits,  please"}

# print(veg)
#
# # UPDATE doesn't return anything
# veg.update(fruit)
#
# print(veg)

# copy method
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)


