# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count('.'))

parrot_List = ["not pinin", "no more", "a stiff", "bereft of live"]

parrot_List.append("A Norwegian Blue")
for state in parrot_List:
    print("This parrot is: " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print('\n')
numbers = even + odd
# numbers.sort()
# print(numbers)
# python can use built in function sorted which return the sorted lists
newSortedList = sorted(numbers)
print(newSortedList)

if newSortedList == numbers:
    print("The lists are equal")
else:
    print("The lists are not equal")

if newSortedList == sorted(numbers):  # sorted(numbers) return the sorted list
    print("The lists are equal")
else:
    print("The lists are not equal")
