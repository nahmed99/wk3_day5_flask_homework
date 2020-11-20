from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player