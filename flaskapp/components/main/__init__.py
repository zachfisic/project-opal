from flask import Blueprint

main = Blueprint('main', __name__)

from flaskapp.components.main import routes