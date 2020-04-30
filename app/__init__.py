from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    #Initializing application
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    #Initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app, url_prefix = '/authentication')
    login_manager.init_app(app)

    #Register Blueprint
    from .main import main 
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth)

    #Setup configurations
    from .request import configure_request
    configure_request(app)

    return app
