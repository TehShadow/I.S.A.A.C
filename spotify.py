import json
import requests
import re



def get_token():
    f = open(".spotipyoauthcache")
    token_info_string = f.read()
    f.close()
    token_info = json.loads(token_info_string)
    token = token_info.get("access_token")
    return token


headers = {
        'Authorization': f'Bearer {get_token()}'
    }

def pause_spotify():
    r = requests.put('https://api.spotify.com/v1/me/player/pause' ,headers=headers)
    print(r)
    print(r.content)

def Start_Resume():
    r = requests.put('https://api.spotify.com/v1/me/player/play' ,headers=headers)
    print(r)
    print(r.content)

def volume(number):
    r = requests.put('https://api.spotify.com/v1/me/player/volume' ,headers=headers ,
     params={
        "volume_percent": number
    })
    print(r)
    print(r.content)
    
def previous():
    r = requests.post('https://api.spotify.com/v1/me/player/previous' ,headers=headers)
    print(r)
    print(r.content)

def next():
    r = requests.post('https://api.spotify.com/v1/me/player/next' ,headers=headers)
    print(r)
    print(r.content)

def shuffle():
    r = requests.put('https://api.spotify.com/v1/me/player/shuffle' ,headers=headers,
    params={
        "state":"true"
    })
    print(r)
    print(r.content)

def search_Spotify(query, type="track",limit=10):
    r = requests.get("https://api.spotify.com/v1/search" , headers=headers ,
    params={
        "query": query,
        "type":type,
        "limit":1
    } )
    print(r)
    print(r.content)

    result = r.content
    result = json.loads(result)
    trackURI = result["tracks"]["items"][0]["uri"]
    trackName = result["tracks"]["items"][0]["name"]
    artistName = result["tracks"]["items"][0]["artists"][0]["name"]

    track = {
        "track":trackURI,
        "trackName":trackName,
        "artistName":artistName
    }
    return(track)

def add_to_queue(uri):
    r = requests.post('https://api.spotify.com/v1/me/player/queue' ,headers=headers,
    params={
        "uri":uri
    })
    print(r)
    print(r.content)



def get_current_track():
    r = requests.get("https://api.spotify.com/v1/me/player" , headers=headers)

    print(r)
    result = r.content
    result = json.loads(result)
    uri = result["context"]["uri"]
    id = re.split("([^:]*$)",uri)
    print(uri)
    print(id[1])
    return id[1]

def Save():
    ids = get_current_track()
    r = requests.put("https://api.spotify.com/v1/me/tracks" , headers=headers,
    params={
        "ids": [f"ids={ids}"]
    })
    print(r)
    print(r.content)