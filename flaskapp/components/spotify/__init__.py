from flask import Blueprint

spotify = Blueprint('spotify', __name__, url_prefix='/spotify')

from flaskapp.components.spotify.graphs import graphs as graphs_bp
spotify.register_blueprint(graphs_bp)

from flaskapp.components.spotify.discover import discover as discover_bp
spotify.register_blueprint(discover_bp)

from flaskapp.components.spotify import routes