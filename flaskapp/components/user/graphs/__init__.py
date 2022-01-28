from flask import Blueprint

graphs = Blueprint('graphs', __name__, url_prefix='/graphs')

from flaskapp.components.user.graphs import routes