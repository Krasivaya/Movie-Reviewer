from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from config import config_options

# Instances
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)
mail = Mail()
simple = SimpleMDE()

def create_app(config_name):

    #Initializing application
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    #Initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    #Register Blueprint
    from .main import main 
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth,url_prefix = '/authentication')

    #Setup configurations
    from .request import configure_request
    configure_request(app)

    #Configure UploadSet
    configure_uploads(app, photos)

    return app
