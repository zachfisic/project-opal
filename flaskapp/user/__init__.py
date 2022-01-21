from flask import Blueprint

bp = Blueprint('user', __name__)

from flaskapp.user import routes