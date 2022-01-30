from cgi import test
from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    print("You are entering via def index")

    return render_template('index.html')

@app.route('/<choice_1>/<choice_2>')
def game(choice_1, choice_2):
    return Game.play_game(choice_1, choice_2)
    