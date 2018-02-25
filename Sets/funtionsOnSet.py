even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
square_tuples = (4, 9, 16, 25)
square = set(square_tuples)
# print(square)
# print(len(square))
#
# print(even.union(square))
# print(len(even.union(square)))
#
# print("*" * 40)
# print(even.intersection(square))
# print(even & square)

print(sorted(even))
print(sorted(square))

print("even minus squares")
print(sorted(even.difference(square)))
print(sorted(even - square))

print(("=" * 40))
even.difference_update(square)
print(sorted(even))