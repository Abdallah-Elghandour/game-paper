from flask import Flask
from blueprint.bp_game import bp_game
from blueprint.bp_game_ahmet import bp_game_ahmet
from blueprint.bp_player import bp_player
from blueprint.bp_player_ahmet import bp_player_ahmet

app = Flask(__name__)
app.register_blueprint(bp_game)
app.register_blueprint(bp_player)
app.register_blueprint(bp_player_ahmet)
app.register_blueprint(bp_game_ahmet)