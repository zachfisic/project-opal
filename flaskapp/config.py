import os
from dotenv import load_dotenv

load_dotenv()

def get_cache_dir():
    """Gets the directory used for cached OAuth Spotify tokens.

    The directory is created if it does not exist.

    Returns:
        The directory of the Spotify cache folder
    """
    caches_folder = './.spotify_caches/'
    if not os.path.exists(caches_folder):
        os.makedirs(caches_folder)
    return caches_folder
    

class Config(object):
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = './.flask_session/'
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET= os.environ['SPOTIPY_CLIENT_SECRET']
    SPOTIPY_REDIRECT_URI= os.environ['SPOTIPY_REDIRECT_URI']
    SPOTIPY_SCOPES_READ_ALL='user-read-playback-state user-read-currently-playing user-read-private user-read-email user-follow-read user-library-read user-read-playback-position user-top-read user-read-recently-played playlist-read-collaborative playlist-read-private'

class ProductionConfig(Config):
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']
    VERSION = 'production'

class DevelopmentConfig(Config):
    SECRET_KEY = os.urandom(64)
    VERSION = 'development'