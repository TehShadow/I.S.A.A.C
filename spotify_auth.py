from flask import Flask
from flask import render_template
from flask import request
import spotipy
from spotipy import oauth2
from spotipy_config import CLIENT_ID , CLIENT_SECRET ,CACHE,SPOTIPY_REDIRECT_URI ,SCOPE




app = Flask(__name__)
sp_oauth = oauth2.SpotifyOAuth( client_secret=CLIENT_SECRET , client_id=CLIENT_ID , redirect_uri=SPOTIPY_REDIRECT_URI , scope=SCOPE , cache_path=CACHE )
cache_token = sp_oauth.get_access_token()
print(cache_token)

@app.route("/")
def home():

    access_token = ""

    token_info = sp_oauth.get_cached_token()


    if token_info:
        print ("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print ("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print ("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)
        results = sp.current_user()
        shutdown_server()
        return results

    else:
        htmlForLoginButton()
        shutdown_server()
        


def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(host='localhost', port=3000)