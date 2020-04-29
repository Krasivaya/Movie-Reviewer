from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

#Get API Key
api_key = app.config['MOVIE_API_KEY']

#Get Movie Base URL
base_url = app.config['MOVIE_API_BASE_URL']