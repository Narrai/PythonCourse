even = set(range(0, 40, 2))
# print(sorted(even))
square_tuples = (4, 16)
square = set(square_tuples)
# print(sorted(square))
#
# print("symmetric even minus square")
# print(sorted(even.symmetric_difference(square)))
#
# print("squares minus even")
# print(sorted(square.symmetric_difference(even)))

# square.discard(4)
# square.remove(16)
# square.discard(8)  # does not raise error
# print(square)
# try:
#     square.remove(8)  # does raise error
# except KeyError:
#     print("The item 8 is not in the set!")

# SUBSET AND SUPERSET
if square.issubset(even):
    print("square is subset of even")

if even.issuperset(square):
    print("even is superset of square")