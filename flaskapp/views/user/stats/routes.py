from flask import render_template
from flaskapp.views.auth.func import authorize
from flaskapp.views.user.stats import stats

@stats.route('/current_user')
@authorize
def current_user(spotify):
    current_user = spotify.current_user() # alias for spotify.me()
    return current_user



@stats.route('/current_user_playing_track')
@authorize
def current_user_playing_track(spotify):
    current_user_playing_track = spotify.current_user_playing_track()
    if current_user_playing_track:
        return current_user_playing_track
    return "No track currently playing."



@stats.route('/current_playback')
@authorize
def current_playback(spotify):
    current_playback = spotify.current_playback()
    if current_playback:
        return current_playback
    return "No track currently playing."
    # return render_template('top_artists.html', artists=artists)



@stats.route('/currently_playing')
@authorize
def currently_playing(spotify):
    currently_playing = spotify.currently_playing()
    if currently_playing:
        return currently_playing
    return "No track currently playing."
    # return render_template('top_artists.html', artists=artists)



@stats.route('/current_user_top_artists')
@authorize
def current_user_top_artists(spotify):
    current_user_top_artists = spotify.current_user_top_artists(time_range='short_term', limit=50)
    artists = {
        "st_items": current_user_top_artists['items']
    }
    return render_template('current_user_top_artists.html', artists=artists)



@stats.route('/current_user_followed_artists')
@authorize
def current_user_followed_artists(spotify):
    current_user_followed_artists = spotify.current_user_followed_artists(limit=50)
    return current_user_followed_artists



@stats.route('/current_user_playlists')
@authorize
def current_user_playlists(spotify):
    current_user_playlists = spotify.current_user_playlists(limit=50)
    return current_user_playlists



@stats.route('/current_user_recently_played')
@authorize
def current_user_recently_played(spotify):
    current_user_recently_played = spotify.current_user_recently_played(limit=50)
    return current_user_recently_played



@stats.route('/current_user_saved_albums')
@authorize
def current_user_saved_albums(spotify):
    current_user_saved_albums = spotify.current_user_saved_albums(limit=50)
    return current_user_saved_albums