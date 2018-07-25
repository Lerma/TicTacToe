from board import Board
from player import Player, RealPlayer
from training.population import ai_play_game

print('Hello world!')
while True:
    if input("New game? (y/n):") == 'n':
        break
    b = Board()
    ai = Player()
    ai.load('training/trained2')
    player = RealPlayer()
    ai_play_game(player, ai)
