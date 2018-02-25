import pickle
# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the Rug"),
#            (2, "Pshyco"),
#            (3, "Mayhem"),
#            (4, "Kentish Town Waltz")))
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

#================================================================#
# with open("imelda.pickle", 'rb') as imeldaPickle:
#     imelda2 = pickle.load(imeldaPickle)
#
# print(imelda2)
#
# album, artist, year, tracks = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in tracks:
#     track_number, track_title = track
#     print(track_number, track_title)

#==================================================================#

# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the Rug"),
#            (2, "Pshyco"),
#            (3, "Mayhem"),
#            (4, "Kentish Town Waltz")))
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)
#     pickle.dump(even, pickle_file)
#     pickle.dump(odd, pickle_file)
#     pickle.dump(2999, pickle_file)
#
with open("imelda.pickle", 'rb') as imeldaPickle:
    imelda2 = pickle.load(imeldaPickle)
    even_list = pickle.load(imeldaPickle)
    odd_list = pickle.load(imeldaPickle)
    x = pickle.load(imeldaPickle)

print(imelda2)

album, artist, year, tracks = imelda2

print(album)
print(artist)
print(year)
for track in tracks:
    track_number, track_title = track
    print(track_number, track_title)

print('*' * 50)

for i in even_list:
    print(i)
print('*' * 50)
for o in odd_list:
    print(o)
print('*' * 50)
print(x)


# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")