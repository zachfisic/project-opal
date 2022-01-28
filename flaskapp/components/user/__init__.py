from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

from flaskapp.components.user.stats import stats as stats_bp
user.register_blueprint(stats_bp)

from flaskapp.components.user.graphs import graphs as graphs_bp
user.register_blueprint(graphs_bp)

from flaskapp.components.user import routes