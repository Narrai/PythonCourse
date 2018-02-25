a_string = "this is \na string\t\tand tabbed"
print(a_string)
raw_string = r"this is \na string\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)
backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

# error_string = r"this string ends with \"
"""
raw_string is introduced to disable the escape characters and mainly for regular 
expression. Python treat \ at the end to escape double quote and results in error, so 
use correctly even with the raw string use double slash (\\)
"""