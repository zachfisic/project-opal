from ensurepip import bootstrap
from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from flaskapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)
Session(app)
Bootstrap(app)
from flaskapp import routes