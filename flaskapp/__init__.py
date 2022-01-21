from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from flaskapp.config import ProductionConfig, DevelopmentConfig

# from flaskapp.auth import bp as auth_bp

session = Session()
bootstrap = Bootstrap()

def create_app(config_class=DevelopmentConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    session.init_app(app)
    bootstrap.init_app(app)

    from flaskapp.user import bp as user_bp
    app.register_blueprint(user_bp)
    
    
    return app