import spotipy as sp
from flask import request, current_app, redirect, url_for
from flaskapp.auth import auth
from flaskapp.auth.func import session_cache_path


@auth.route('/auth/spotify/callback')
def api_callback():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'], cache_handler=cache_handler, show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"), as_dict=False)
        return redirect(url_for('main.index'))