import os
import uuid
from webbrowser import get
import spotipy as sp
from flask import session, request, redirect, render_template, url_for, current_app
from flaskapp.config import get_cache_dir
from flaskapp.user import bp
from functools import wraps


def session_cache_path():
    try:
        return get_cache_dir() + session.get('uuid')
    except:
        print('session ID not found, returning to index')
        return redirect(url_for('user.index'))


def get_auth_spotify():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect(url_for('user.index'))
    return sp.Spotify(auth_manager=auth_manager)


@bp.route('/sign_out')
def sign_out():
    try:
        # Remove the cache file so that a new user can authorize.
        os.remove(session_cache_path())
        session.clear()
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")
    return redirect(url_for('user.index'))


@bp.route('/')
def index():
    if not session.get('uuid'):
        session['uuid'] = str(uuid.uuid4())
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'] ,cache_handler=cache_handler, show_dialog=True)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return f'<h2><a href="{auth_url}">Sign in</a></h2>'
    spotify = sp.Spotify(auth_manager=auth_manager)
    user = {
        'username': spotify.me()["display_name"]
    }
    return render_template('index.html', user=user)



@bp.route('/auth/spotify/callback')
def api_callback():
    cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'], cache_handler=cache_handler, show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"), as_dict=False)
        return redirect(url_for('user.index'))
    


@bp.route('/current_user')
def current_user():
    spotify = get_auth_spotify()
    # alias for spotify.me()
    current_user = spotify.current_user()
    return current_user



@bp.route('/current_user_playing_track')
def current_user_playing_track():
    
    spotify = get_auth_spotify()
    current_user_playing_track = spotify.current_user_playing_track()
    
    if current_user_playing_track:
        return current_user_playing_track
    return "No track currently playing."



@bp.route('/current_playback')
def current_playback():

    spotify = get_auth_spotify()
    current_playback = spotify.current_playback()

    if current_playback:
        return current_playback
    return "No track currently playing."
    # return render_template('top_artists.html', artists=artists)



@bp.route('/currently_playing')
def currently_playing():

    spotify = get_auth_spotify()
    currently_playing = spotify.currently_playing()

    if currently_playing:
        return currently_playing
    return "No track currently playing."
    # return render_template('top_artists.html', artists=artists)



@bp.route('/current_user_top_artists')
def current_user_top_artists():
    spotify = get_auth_spotify()
    current_user_top_artists = spotify.current_user_top_artists(time_range='short_term', limit=50)
    artists = {
        "st_items": current_user_top_artists['items']
    }
    return render_template('current_user_top_artists.html', artists=artists)



@bp.route('/current_user_followed_artists')
def current_user_followed_artists():
    spotify = get_auth_spotify()
    current_user_followed_artists = spotify.current_user_followed_artists(limit=50)
    return current_user_followed_artists



@bp.route('/current_user_playlists')
def current_user_playlists():
    spotify = get_auth_spotify()
    current_user_playlists = spotify.current_user_playlists(limit=50)
    return current_user_playlists



@bp.route('/current_user_recently_played')
def current_user_recently_played():
    spotify = get_auth_spotify()
    current_user_recently_played = spotify.current_user_recently_played(limit=50)
    return current_user_recently_played



@bp.route('/current_user_saved_albums')
def current_user_saved_albums():
    spotify = get_auth_spotify()
    current_user_saved_albums = spotify.current_user_saved_albums(limit=50)
    return current_user_saved_albums