from flask import render_template
from app import app
from .request import get_movies, get_movie

#Views
@app.route('/')
def index():
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template(
        'index.html', 
        title = title, 
        popular = popular_movies,
        upcoming = upcoming_movies,
        now_showing = now_showing_movies)

#Movie details
@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template(
        'movie.html', 
        title = title,
        movie = movie)