from flask import Blueprint, request, redirect, url_for
import json
from flask import jsonify
from DataBase.db import r

bp_player = Blueprint("bp_player", __name__)
db = []
@bp_player.route('/player', methods=['GET', 'POST'])
def player():
    global bd
    found = False
    
    playerjs = request.json
    db = r.lrange("players",0,-1)
    for i, x in enumerate(db):
        db[i] = json.loads(x)
        if playerjs["name"] == db[i]["name"]:
            found = True
            player = db[i]

    if not found:
        playerjs["win"] = 0
        player_json = json.dumps(playerjs)
        r.rpush("players", player_json)
        i +=1
        player = playerjs

    player =  f"{player}"
    #result = game(playerjs['player'], player, i)
    return jsonify(data=player,status='OK')

    
