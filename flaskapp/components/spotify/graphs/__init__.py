from flask import Blueprint

graphs = Blueprint('graphs', __name__, url_prefix='/graphs')

from flaskapp.components.spotify.graphs import routes