from flask import Blueprint

stats = Blueprint('stats', __name__, url_prefix='/stats')

from flaskapp.views.user.stats import routes