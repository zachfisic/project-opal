from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from flaskapp.config import DevelopmentConfig

session = Session()
bootstrap = Bootstrap()

def create_app(config_class=DevelopmentConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    session.init_app(app)
    bootstrap.init_app(app)

    # Register bluprints
    from flaskapp.views.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from flaskapp.views.main import main as main_bp
    app.register_blueprint(main_bp)

    from flaskapp.views.user import user as user_bp
    app.register_blueprint(user_bp)
    
    return app