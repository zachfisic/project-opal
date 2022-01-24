from flask import Blueprint

main = Blueprint('main', __name__)

from flaskapp.views.main.graphs import graphs as graphs_bp
main.register_blueprint(graphs_bp)

from flaskapp.views.main import routes