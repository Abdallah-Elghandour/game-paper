from flask import Blueprint, request, redirect, url_for
from DataBase.db import es

bp_player= Blueprint("bp_player", __name__)
db = []
@bp_player.route('/player', methods=['GET', 'POST'])
def player_ahmet():
    playerjs = request.json
    found = es.search(index="players", query={"match":{"name":playerjs["name"]}})
   
    if found['hits']['hits'] == []:
        document = {"name":playerjs["name"], "win": 0, "playing_counter": 0}
        es.index(index="players", document=document, id=int(es.cat.count(index="players", format="json")[0]['count']) + 1)
        return redirect(url_for("bp_game.index",player=int(es.cat.count(index="players", format="json")[0]['count']) + 1))
    
    return redirect(url_for("bp_game.index",player=int(found['hits']['hits'][0]['_id'])))
