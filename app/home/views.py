# app/home/views.py

from flask import render_template

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    user = {'username': 'jQN'}
    return render_template('home/index.html', title="Welcome ", user=user)