from flask import Blueprint

main = Blueprint('main', __name__)

from flaskapp.main import routes