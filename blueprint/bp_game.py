from flask import Blueprint, request
from structure.game import game

bp_game = Blueprint('bp_game', __name__)

@bp_game.route('/game/<int:player>', methods=['POST', 'GET'])
def index(player):
    round_js = request.json
    player_round = round_js['player']
    result = game(player_round, player)
    return result