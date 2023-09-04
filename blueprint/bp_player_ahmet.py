from flask import Blueprint, request, redirect, url_for
import json
from flask import jsonify
from DataBase.db import r

bp_player_ahmet = Blueprint("bp_player_ahmet", __name__)
db = []
@bp_player_ahmet.route('/player_ahmet', methods=['GET', 'POST'])
def player_ahmet():
    playerjs = request.json
    test = r.get(playerjs['name'])
    if test == None:
        r.set(playerjs['name'],0)
        return jsonify(data={"player":playerjs['name'],"win":0})
    else:
        return jsonify(data={"player": playerjs['name'], "win": int(test)})