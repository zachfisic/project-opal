import spotipy as sp
from flask import render_template
from flaskapp.components.spotify import spotify


@spotify.route('/')
def index():
    """Base route for Spotify graphs.

    Returns:
        an HTML template
    """
    return render_template('spotify.html')
    