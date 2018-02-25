# myList = ['a', 'b', 'c', 'd']
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"
# newString = ''
# newString = ", ".join(myList)
# newString1 = ", ".join(letters)
# newString2 = " mississippi ".join(numbers)
# print(newString)
# print(newString1)
# print(newString2)

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are ina valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableTickets = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     availableTickets += direction + ", "
    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + availableTickets + ": ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go in that direction")