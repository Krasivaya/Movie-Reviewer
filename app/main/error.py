from flask import render_template
from app import app

#Errors
@app.errorhandler(404)
def four_o_four(error):
    return render_template(
        'fourOfour.html'
    ),404