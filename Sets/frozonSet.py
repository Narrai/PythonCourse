"""Frozen set is immutable and hence it does not support add and other methods
and hence it can be used as the dictionary keys"""

even = frozenset(range(0, 100, 2))
# even.add(3)

"""Create a program that takes some text and returns a list of 
all the characters in the text that are not vowels, sorted in 
alphabetical order.
you can either enter the text from the keyboard or initialise a string variable with the string."""

sampleText = "Python is a very powerful language"
vowels = frozenset("aeiou")
final_set = set(sampleText).difference(vowels)
print(final_set)

finalList = sorted(final_set)
print(finalList)