from flask import Flask
from blueprint.bp_game import bp_game
from blueprint.bp_players import bp_players
from blueprint.bp_player import bp_player


app = Flask(__name__)
app.register_blueprint(bp_game)
app.register_blueprint(bp_player)
app.register_blueprint(bp_players)
