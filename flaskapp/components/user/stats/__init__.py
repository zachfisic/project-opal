from flask import Blueprint

stats = Blueprint('stats', __name__, url_prefix='/stats')

from flaskapp.components.user.stats import routes