from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    #Initializing application
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    #Initialize flask extensions
    bootstrap.init_app(app)

    #Register Blueprint
    from .main import main 
    app.register_blueprint(main)

    #Setup configurations
    from .request import configure_request
    configure_request(app)

    return app
