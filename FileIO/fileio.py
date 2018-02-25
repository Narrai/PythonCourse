# jabber = open("C:\\Desktop\\sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():  # it looks for the jabberwock and print that line only
#         print(line, end="")
# jabber.close()

# with 'with' does not need to close the file explicitly
# with open("C:\\Desktop\\sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')


# BY USING READLINE() reads line by line
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# BY USING READLINES() which returns the list
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end='')

# Reversing the file by using readlines() and read()
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
for line in lines[::-1]:
    print(line, end='')
print("=" * 60)
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
for line in lines[::-1]:
    print(line, end='')