from flask import Blueprint, request
from structure.game import game
bp_game = Blueprint('bp_game', __name__)

@bp_game.route('/game/<player>/<int:index>', methods=['POST', 'GET'])
def index(player, index):
    round_js = request.json
    result = game(round_js['player'], player, index)
    return result