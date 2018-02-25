# print(range(0, 5, 2) == range(0, 6, 2))  # both return same contain
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print('*' * 5)
# for i in range(99, 0, -2):
#     print(i)
#
# for i in range(0, 100, -2):
#     print(i)  # return nothing, make sure start and end value should be reversed while decrementing

# printing reverse string
backString = "A lazy fox jumps over a lazy dog"
print(backString[::-1])

o = range(0, 100, 4)
print(o)
for i in o:
    print(i)
p = o[::10]
print(p)

for i in p:
    print(i)


