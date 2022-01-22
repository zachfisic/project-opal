import spotipy as sp
from functools import wraps
from flask import session, redirect, url_for
from flaskapp.config import get_cache_dir

def session_cache_path():
    try:
        return get_cache_dir() + session.get('uuid')
    except:
        print('session ID not found, returning to index')
        return redirect(url_for('main.index'))


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
        auth_manager = sp.oauth2.SpotifyOAuth(cache_handler=cache_handler)
        if not auth_manager.validate_token(cache_handler.get_cached_token()):
            return redirect(url_for('main.index'))
        spotify = sp.Spotify(auth_manager=auth_manager)
        return f(spotify, *args, **kws)            
    return decorated_function