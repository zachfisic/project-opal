import spotipy as sp
from flask import request, current_app, redirect, url_for
from flaskapp.views.auth import auth
from flaskapp.views.auth.func import session_cache_path


@auth.route('/auth/spotify/callback')
def api_callback():
    """Handles the OAuth redirect process from Spotify.

    The incoming `code` from request.args is used to get an access token, which will be saved at the specified cache path. The user is directed to the index page which will display the appropriate template.
    
    Returns:
        A redirect to the index page
    """
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'], cache_handler=cache_handler, show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"), as_dict=False)
        return redirect(url_for('main.index'))