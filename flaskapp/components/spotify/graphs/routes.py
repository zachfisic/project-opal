import spotipy
from flask import render_template
from flaskapp.components.spotify.graphs import graphs


@graphs.route('/')
def index():
    pass
