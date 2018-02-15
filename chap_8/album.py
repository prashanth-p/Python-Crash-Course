import sys
print(sys.version)


def make_album(artist_name, album_title, album):
    album[album_title] = artist_name
    return album


if __name__ == '__main__':
    album = {}
    print(make_album("Akon", "Freedom", album))
    print(make_album("Beyonce", "7/11", album))
