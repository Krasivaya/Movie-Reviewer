from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask(__name__)

#Setup configurations
app.config.from_object(DevConfig)


from app import views