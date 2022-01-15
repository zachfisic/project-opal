from json import load
import os
from dotenv import load_dotenv

load_dotenv()

def get_cache_dir():
    caches_folder = './.spotify_caches/'
    if not os.path.exists(caches_folder):
        os.makedirs(caches_folder)
    return caches_folder
    

class Config(object):
    SECRET_KEY = os.urandom(64)
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = './.flask_session/'
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET=['SPOTIPY_CLEINT_SECRET']
    SPOTIPY_REDIRECT_URI=['SPOTIPY_REDIRECT_URI']
    SPOTIPY_SCOPES_READ_ALL='user-read-playback-state user-read-currently-playing user-read-private user-read-email user-follow-read user-library-read user-read-playback-position user-top-read user-read-recently-played playlist-read-collaborative playlist-read-private'
