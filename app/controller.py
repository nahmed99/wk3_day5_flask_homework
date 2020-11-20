# from flask import render_template, request, redirect - don't need request and redirect for the simple 'GET' in the initial, MVP part of the application
from flask import render_template
from app import app
from app.models.game import Game
from app.models.player import Player


# Controller routes match HTTP routes TO functions.

# The controller sits and listens, waiting for requests that will come in

# This defaults to a GET request
@app.route('/') # This listens for 'requests' to the home/root
def index():
    # This and other below are normal python functions...
    return render_template('index.html', title="Home")


@app.route('/<hand1>/<hand2>')
def play_game(hand1, hand2):
    return f"Hello, {hand1} {hand2}"