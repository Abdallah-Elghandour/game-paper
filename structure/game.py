
from DataBase.db import es
import random

def game(player_round, player):
    lst = ['Rock', 'Paper', 'Scissors']
    bot = random.choice(lst)
    searchPlayer = es.search(index="players",query={"match":{"_id":player}})
    if player_round == bot:
        result = "No one win"
    elif (player_round == 'Paper' and bot == 'Rock') or (player_round == 'Rock' and bot == 'Scissors') or (player_round == ' Scissors' and bot == 'Paper'):
        result = "Player Wins"
        winCounter = searchPlayer["hits"]["hits"][0]["_source"]['win']
        es.update(index="players", id=player, doc={'win': winCounter + 1})
    else:
        result = "bot Wins"
        
    playingCounter = searchPlayer["hits"]["hits"][0]["_source"]["playing_counter"]
    es.update(index="players", id=player, doc={'playing_counter': playingCounter + 1})
    win = {"player":player_round, "bot":bot, "win": result}
    return win

