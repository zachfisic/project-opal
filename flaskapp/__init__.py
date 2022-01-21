from ensurepip import bootstrap
import os
from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from flaskapp.config import ProductionConfig, DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

Session(app)
Bootstrap(app)
from flaskapp import routes