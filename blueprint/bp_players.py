from flask import Blueprint
from DataBase.db import es
bp_players = Blueprint('bp_players', __name__)

@bp_players.route("/players", methods=['GET'])
def players():
    result = []
    docs = es.search(index='players', query={"match_all": {}})
    for doc in docs['hits']["hits"]:
        result.append(doc["_source"])
    return result
