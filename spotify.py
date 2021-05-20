from json import load
import dotenv
import requests
from requests.api import head
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
token = os.getenv('TOKEN')

print(token)

def pause_spotify():
    headers = {
        'Authorization': f'Bearer {token}'
    }
    r = requests.put('https://api.spotify.com/v1/me/player/pause' ,headers=headers)
    print(r)
    print(r.content)