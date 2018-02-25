"""Set in python is unordered and does not duplicate, but items aren't accessed
by keys, it looks like set are similar to collection of dictionaries keys, and set members are
hashed as dictionaries keys are. Element in the sets are immutable objects just like dictionaries keys,
and support union and intersection operation. Useful to cleaning data.
"""

# # Create set simply by using curly braces
# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("*" * 40)
#
# # By passing list in the set functions
# wild_animals = set(["lion", "tiger", "panther", "elephant"])
# print(wild_animals)
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

"""While creating empty set we need to use 
set function otherwise it creates empty dictionary if we use empty braces"""
empty_set = set()
empty_set1 = {}
# empty_set.add("a")
# empty_set1.add("a")  # throws exception

"""In the set constructor we can pass any iterable objects like tuples, range"""
even = set(range(0, 40, 2))
print(even)

square_tuples = (4, 9, 16, 25)
squares = set(square_tuples)
print(squares)

string = "abcdefghijklmnopqrstuvwxyz"
string_set = set(string)
print(string_set)
