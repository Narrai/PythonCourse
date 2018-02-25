number = "6, 123, 526, 865, 201"
cleanNumber = ""

for char in number:
    if char in "0123456789":
        cleanNumber = cleanNumber + char

newNumber = int(cleanNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a siff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(1, 100, 10):
    print("i is {} ".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format( i, j, i * j), end=' ')
    # print("=================")