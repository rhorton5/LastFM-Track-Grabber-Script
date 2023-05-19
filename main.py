from lastFmPython import LastFmPython

if __name__ == '__main__':
    lfm = LastFmPython()
    artist = input('Enter the name of the artist: ')
    album = input('Enter the name of the album: ')
    lfm.getArtistInformation(artist,album)
    

    


