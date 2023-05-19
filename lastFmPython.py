import requests,json

class LastFmPython():
    def __init__(self):
        self.apiKey = self.importAPIKey()
        self.userName = self.importUserName()
        self.format = 'json'
        self.apiURl = 'http://ws.audioscrobbler.com/2.0/'

    def importUserName(self):
        with open('config.json','r') as file:
            data = json.load(file)
            return data['userName']
        
    def importAPIKey(self):
        with open('config.json','r') as file:
            data = json.load(file)
            return data['apiKey']
        
    def getArtistInformation(self,artist=str,album=str):
        albumArtistName = f"{artist} - {album}"
        print('-' * 20 + albumArtistName + '-' * 20)
        print(self.getAlbumInfo(artist,album))
        print('-' * 20 + '-' * len(albumArtistName) + '-' * 20 + '\n')
    
    def getAlbumInfo(self,artist=str,album=str):
            method = 'album.getInfo'
            parameters = {
                    'method': method,
                    'artist': artist,
                    'album': album,
                    'api_key': self.apiKey,
                    'format': 'json',
                    'autocorrect': 1
                }

            response = requests.get(self.apiURl,params=parameters)
            data = response.json()

            try:
                res = ""
                trackNum = 1
                for track in data['album']['tracks']['track']:
                    res += f"{trackNum}. {track['name']}\n"
                    trackNum += 1
                
                return res[:len(res)-1]
            
            except Exception:
                print(f'{album} by {artist} caused an error... make sure you spelt the album and artist correctly.')
                return None