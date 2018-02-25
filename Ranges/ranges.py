
my_string = "abcdefghijklmnopqrstuvwxyz"
# index method

# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals.index(3))
#
# odd = list(range(1, 10000, 2))
# print(odd)
#
# print(odd[985])  # returns value in that index position
# print(odd.index(1971))  # returns index of that value

# sevens = range(7, 1000000, 7)
# x = int(input('Enter a positive number less than one million: '))
# if x in sevens:
#     print("{} is divisible by seven".format(x))

# using slice ranges
# evenRange = range(0, 100)
# my_evenRange = evenRange[::2]
# print(my_evenRange[11])
# print(my_evenRange.index(22))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)
for i in my_range:
    print(i)

print('*' * 45)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))
print(my_range is range(3, 40, 3))
