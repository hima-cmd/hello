'''
Write a function called city_country() that takes in the name of a city 
and its country.The function should return a string formatted like this:
Santiago, Chile
Call your function with at least three city-country pairs, 
and print the value that"s returned .'''

def city_country(city,country):
    display = city + " , " +country
    return(display.title())

print(city_country('delhi','india'))
print(city_country('london', 'uk'))
print(city_country('ny', 'usa'))


def make_album(name,title,notracks=''):
    #build dictionary describing music album
    music_album = {'artist_name':name, 'album_title':title}
    if notracks:#if notracks is not empty string
        music_album['tracks'] = notracks
    return(music_album)

'''
dict_music = make_album('bryan adams', 'here I am')
print(dict_music)
dict_music = make_album('beyonce', 'whatever')
print(dict_music)
dict_music = make_album('jennifer', 'jlo','10')
print(dict_music)
'''
while True:
    print("\nEnter album details.")
    print("(enter 'q' at any time to quit)")
    name = raw_input("Enter Artist Name : ")
    if name =='q':
        break
    title = raw_input("Enter Album Title : ")
    if title == 'q':
        break
    dict_music = make_album(name,title)
    print(dict_music)
print('\nEnd of program.')
