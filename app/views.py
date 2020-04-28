from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template('index.html', title = title)

#Dynamic Routes
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html', id = movie_id)