import os
import uuid
import spotipy as sp
from flask import session, request, redirect, render_template, url_for
from flaskapp import app
from flaskapp.config import get_cache_dir


def session_cache_path():
    try:
        return get_cache_dir() + session.get('uuid')
    except:
        print('session ID not found, returning to index')
        return redirect('/')


@app.route('/')
def index():

    if not session.get('uuid'):
        session['uuid'] = str(uuid.uuid4())

    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=app.config['SPOTIPY_SCOPES_READ_ALL'] ,cache_handler=cache_handler, show_dialog=True)

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return f'<h2><a href="{auth_url}">Sign in</a></h2>'

    
    spotify = sp.Spotify(auth_manager=auth_manager)

    user = {
        'username': spotify.me()["display_name"]
    }
    return render_template('index.html', user=user)


@app.route('/auth/spotify/callback')
def api_callback():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=app.config['SPOTIPY_SCOPES_READ_ALL'], cache_handler=cache_handler, show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"), as_dict=False)
        return redirect('/')
    


@app.route('/current_user')
def current_user():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = sp.Spotify(auth_manager=auth_manager)

    return spotify.current_user()


@app.route('/playlists')
def playlists():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = sp.Spotify(auth_manager=auth_manager)

    return spotify.current_user_playlists()


@app.route('/currently_playing')
def currently_playing():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = sp.Spotify(auth_manager=auth_manager)

    track = spotify.current_user_playing_track()
    
    if not track is None:
        return track
    return "No track currently playing."


@app.route('/sign_out')
def sign_out():
    try:
        # Remove the cache file so that a new user can authorize.
        os.remove(session_cache_path())
        session.clear()
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")
    return redirect('/')