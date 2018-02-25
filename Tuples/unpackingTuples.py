# imelda = 'More Mayhem', 'Imilda May', 1984, (
#     (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
#)
# metallica2 = ['Ride the Lightening', 'Metallica', 1984]
#
# title, artist, year = imelda
# print(title)
# print(artist)
# print(year)

# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for songs in tracks:
#     track, title = songs
#     print('\tTrack Number: {}, Title: {}'.format(track, title))


# IF THE TUPLE CONTAIN LIST AS ITS ITEM, THEN WE CAN APPEND TO THE LIST OR THE CONTAIN OF THE LIST CAN BE CHANGED
imelda = 'More Mayhem', 'Imilda May', 1984, (
    [(1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')]
)
print(imelda)
imelda[3].append((5, 'All For you'))
title, artist, year, tracks = imelda
imelda[3].append((6, 'Eternity'))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print('\tTrack Number: {}, Title: {}'.format(track, title))

