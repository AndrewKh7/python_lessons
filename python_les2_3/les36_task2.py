import requests as req
import json


client_id = '6d3aae889a21d37c4202'
client_secret = '4752959470f834879fbf0632ab64ad38'

# инициируем запрос на получение токена
r = req.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# достаем токен
token = json.loads(r.text)["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

def getArtist(id):
    url = f'https://api.artsy.net/api/artists/{id}'
    res = req.get(url, headers=headers)
    if res.status_code == 200:
        artist = json.loads(res.text)
        return artist
    else:
        print('Error request:', url)
    

if __name__ == '__main__':
    artists = list()
    with open('./artist.txt', encoding='utf-8') as f:
        for line in f:
            artists.append(getArtist(line.strip('\n')))
        artists = sorted(artists, key = lambda a: (a['birthday'],a['sortable_name']))
        for art in artists:
            print(art['sortable_name']) 
