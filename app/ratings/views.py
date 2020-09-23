# app/ratings/views.py

from flask import render_template

from . import ratings


@ratings.route('/ratings')
def ratings():
    """
    Render the ratings template on the /ratings route
    """
    return render_template('ratings/ratings.html', title="Deal Ratings")