
from DataBase.db import r
import random

def game(player_round, player, index):
    lst = ['Rock', 'Paper', 'Scissors']
    bot = random.choice(lst)
    if player_round == bot:
        result = "No one win"
    elif (player_round == 'Paper' and bot == 'Rock') or (player_round == 'Rock' and bot == 'Scissors') or (player_round == ' Scissors' and bot == 'Paper'):
        result = "Player Wins"
        player["win"] += 1
        r.lset("players", index, player)
    else:
        result = "bot Wins"
    win = {"player":player_round, "bot":bot, "win": result}
    return win

def game_2(player_round, player):
    lst = ['Rock', 'Paper', 'Scissors']
    bot = random.choice(lst)
    if player_round == bot:
        result = "No one win"
    elif (player_round == 'Paper' and bot == 'Rock') or (player_round == 'Rock' and bot == 'Scissors') or (player_round == ' Scissors' and bot == 'Paper'):
        result = "Player Wins"
        win_number = r.get(player)
        win_number = int(win_number)
        win_number += 1
        r.set(player,win_number)
    else:
        result = "bot Wins"
    win = {"player":player_round, "bot":bot, "win": result}
    return win