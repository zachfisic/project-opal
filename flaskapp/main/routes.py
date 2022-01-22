import uuid
import spotipy as sp
from flask import session, current_app, render_template
from flaskapp.auth.func import session_cache_path
from flaskapp.main import main

@main.route('/')
def index():
    if not session.get('uuid'):
        session['uuid'] = str(uuid.uuid4())
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'] ,cache_handler=cache_handler, show_dialog=True)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return render_template('opal.html', auth_url=auth_url)
    spotify = sp.Spotify(auth_manager=auth_manager)
    user = {
        'username': spotify.me()["display_name"]
    }
    return render_template('index.html', user=user)