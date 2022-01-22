from flask import Blueprint

auth = Blueprint('auth', __name__)
from flaskapp.auth import routes