locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# exits = [{"Q": 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          {"N": 5, "Q": 0},
#          {"W": 1, "Q": 0},
#          {"N": 1, "W": 2, "Q": 0},
#          {"W": 2, "S": 1, "Q": 0}]
# modifying code and making it dictionary
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + availableExits + ": ").upper()
    print()

    # Parse the user input, using vocabulary dictionary if necessary
    if len(direction) > 1:  # more than one letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
    if direction in exits[loc]:
        loc = exits[loc][direction]
        print("locations is {}".format(loc))
    else:
        print("you cannot go in that direction")

    """ALTERNATIVE WAY FOR SEARCHING BUT IF VOCAB IS BIG, LOOPING VOCAB IS NOT EFFICIENT
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]"""