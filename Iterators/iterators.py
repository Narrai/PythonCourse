string = "1234567890"

# for char in string:
#     print(char, end=' ')

my_iterator = iter(string)
print(my_iterator)  # returns new object of iterator in memory

# To print the actual contains
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# For loop implicitly create iterable object and loop through it

# for char in string:
#     print(char)
# # looping and creating iterable object
# for char in iter(string):
#     print(char, end=' ')

# challenge
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
my_iterator = iter(my_list)
for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)


