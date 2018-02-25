"""When converting a decimal number to binary, you look for the highest power
of 2 smaller than the number and put 1 in that column. You then take the remainder
and repeat the process with the next highest power - putting 1 if it goes into the
remainder and a zero otherwise. Keep repeating the process until you have dealt with
all powers down to 2**0(i.e....1"""

powersOfTwo = []
for power in range(15, -1, -1):
    powersOfTwo.append(2**power)
print(powersOfTwo)

x = int(input("Please enter a number: "))

printing = False
for power in powersOfTwo:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
input("press enter to quit")
