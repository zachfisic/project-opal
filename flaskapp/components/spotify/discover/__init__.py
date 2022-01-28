from flask import Blueprint

discover = Blueprint('discover', __name__, url_prefix='/discover')

from flaskapp.components.spotify.discover import routes