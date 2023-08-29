from flask import Blueprint, request,jsonify
from structure.game import game_2
from DataBase.db import r
bp_game_ahmet = Blueprint('bp_game_ahmet', __name__)

@bp_game_ahmet.route('/game_ahmet/<player>', methods=['POST', 'GET'])
def index(player):
    test = r.get(player)
    if test == None:
        return jsonify(data=['player not exist'])
    else:
        round_js = request.json
        player_round = round_js['player']
        result = game_2(player_round, player)
        return result