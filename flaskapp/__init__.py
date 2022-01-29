from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from flaskapp.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

session = Session()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'
login.login_message = 'Please Log In'

def create_app(config_class=DevelopmentConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    session.init_app(app)
    bootstrap.init_app(app)
    
    # Register bluprints
    from flaskapp.components.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from flaskapp.components.main import main as main_bp
    app.register_blueprint(main_bp)

    from flaskapp.components.spotify import spotify as spotify_bp
    app.register_blueprint(spotify_bp)

    from flaskapp.components.user import user as user_bp
    app.register_blueprint(user_bp)
    
    return app

from flaskapp import models