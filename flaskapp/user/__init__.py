from flask import Blueprint

user = Blueprint('user', __name__)

from flaskapp.user import routes