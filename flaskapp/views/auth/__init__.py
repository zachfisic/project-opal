from flask import Blueprint

auth = Blueprint('auth', __name__)
from flaskapp.views.auth import routes