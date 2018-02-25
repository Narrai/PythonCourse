number = "9, 123, 546, 3562, 120"
cleanNumber = ''

for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanNumber += number[i]  # AugmentedAssignment

newNumber = int(cleanNumber)
print("The number is {}".format(newNumber))
