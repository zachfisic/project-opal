import spotipy as sp
from flask import current_app, render_template
from flaskapp.components.auth.func import session_cache_path, set_session_id
from flaskapp.components.main import main


@main.route('/')
def index():
    """Index route for the application.

    Displays welcome page, with additional information if user has authorized the application to use Spotify data.

    Returns:
        an HTML template
    """
    set_session_id()
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'] ,cache_handler=cache_handler, show_dialog=True)
    
    # if access token doesn't exist or is invalid, return a generic template with the authorization URL
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return render_template('welcome.html', auth_url=auth_url)
    
    # The user has authorized the application, we can generate a Spotify instance with the configured authorization manager
    spotify = sp.Spotify(auth_manager=auth_manager)
    user = {
        'username': spotify.me()["display_name"]
    }
    return render_template('user.html', user=user)