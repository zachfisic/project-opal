from flask import Blueprint

auth = Blueprint('auth', __name__)
from flaskapp.components.auth import routes