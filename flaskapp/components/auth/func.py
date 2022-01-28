import spotipy as sp
import uuid
from functools import wraps
from flask import session, redirect, url_for
from flaskapp.config import get_cache_dir


def set_session_id():
    """Stores a UUID for the Flask session if it doesn't already exist"""

    if not session.get('uuid'):
        session['uuid'] = str(uuid.uuid4())



def session_cache_path():
    """Fetches the location of the cached Spotify token.

    Returns:
        the location of the token, relative to the project's root. If the token cannot be found, the function returns a redirect to the index.
    """
    try:
        return get_cache_dir() + session.get('uuid')
    except:
        print('session ID not found, returning to index')
        return redirect(url_for('main.index'))



def authorize(f):
    """Decorates a function with Spotify OAuth flow.

    Validates the session's OAuth token and either executes the wrapped function or redirects the user to the index page

    Args:
        f: the function to decorate
    
    Returns:
        A decorator. If authorized, the wrapped function is provided an instance of an authorized Spotify module to work with
    """
    @wraps(f)
    def decorated_function(*args, **kws):
        # The authorization manager should use the token available at the provided cache path.
        cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
        auth_manager = sp.oauth2.SpotifyOAuth(cache_handler=cache_handler)
        if not auth_manager.validate_token(cache_handler.get_cached_token()):
            return redirect(url_for('main.index'))
        spotify = sp.Spotify(auth_manager=auth_manager)
        return f(spotify, *args, **kws)
    return decorated_function



def use_client_credentials(f):
    """Decorates a function with Spotify client credentials.

    The Client Credentials flow does not require user authentication.

    Returns:
        A decorator. The wrapped function provides an instance of Spotify that can only work with non-user related Spotify data.
    """
    @wraps(f)
    def decorated_function(*args, **kws):
        cc_manager = sp.oauth2.SpotifyClientCredentials()
        spotify = sp.Spotify(client_credentials_manager=cc_manager)
        return f(spotify, *args, **kws)
    return decorated_function