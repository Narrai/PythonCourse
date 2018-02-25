# list_1 = []
# list_2 = list()
# print("List_1: {}".format(list_1))
# print("List_2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal!")
#
# # by using list() function
#
# print(list('The lists are equal'))

even = [2, 4, 6, 8]
# another_even = even
# print(another_even is even)
#
# # by using constructor totally new list is created
# another_even1 = list(even)
# print(another_even1 is even)
#
# # contain are same
# print(another_even1 == another_even)
# another_even1.sort(reverse=True)
# print(another_even1)
# another_even.sort(reverse=True)

odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)

