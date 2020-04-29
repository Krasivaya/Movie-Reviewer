from flask import render_template
from . import main

#Errors
@main.app_errorhandler(404)
def four_o_four(error):
    return render_template(
        'fourOfour.html'
    ),404