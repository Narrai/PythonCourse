# Tuples are immutable but list are  mutable
# t = "a", "b", "c"
# print(t)
#
# print('a', 'b', 'c')
# print(('a', 'b', 'c'))

# welcome = "Welcome to my nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Night Flight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightening", "Metallica", 1984
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Master of puppets" # tuples does not support assigning new value
#
# # contain of tuple cannot be change but variable can be assigned to new object of that type
# # In this case we create the variable imelda referencing the new tuple object
# # list are intended to hold homogeneous element but tuples are intended to hold heterogeneous object
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
#
# metallica2 = ["Ride the Lighning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# UNPACKING TUPLE
title, artist, year = imelda
print(title)
print(artist)
print(year)

