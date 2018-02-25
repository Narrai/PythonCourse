import shelve
locations = shelve.open('locations')
vocabulary = shelve.open('vocabulary')

loc = '1'
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    directions = input("Available exits are " + availableExits + ": ").upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(directions) > 1:
        words = directions.split()
        for word in words:
            if word in vocabulary:
                directions = vocabulary[word]
                break
    if directions in allExits:
        loc = allExits[directions]
    else:
        print("You cannot go in that direction")
vocabulary.close()
locations.close()
