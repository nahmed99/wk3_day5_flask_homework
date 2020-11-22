from flask import render_template, redirect
from app import app
from app.models.game import Game
from app.models.player import Player


# Controller routes match HTTP routes TO functions.

# The controller sits and listens, waiting for requests that will come in


@app.route('/') # This listens for 'requests' to the home/root
def index():
    # This will redirect the user to the welcome page...
    return redirect("/welcome")


@app.route('/welcome') # This listens for 'requests' to the home/root
def welcome():
    # This and other below are normal python functions...
    return render_template('index.html', title="Welcome")


@app.route('/<hand1>/<hand2>')
def play_game(hand1, hand2):
    player_1 = Player("Player 1", hand1)
    player_2 = Player("Player 2", hand2)
    game = Game(player_1, player_2)

    result = f"Player 1 had {hand1} and player 2 had {hand2}. "

    if game.check_winner():
        result += "The winner is player 1"
    elif game.check_winner() == None:
        result += "It is a DRAW!"
    else: 
        result += "The winner is player 2"

    return render_template('result.html', title="Result", result=result)