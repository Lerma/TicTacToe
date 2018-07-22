from __future__ import annotations

from copy import deepcopy
from typing import List

from board import Board, print_board
from player import Player


def ai_play_game(player1: Player, player2: Player):
    b = Board()
    player1.side = -1
    player2.side = 1
    current_player = player1
    while not b.game_over:
        move_successful = False
        while not move_successful:
            move_successful = b.move(current_player.side, current_player.make_move(b.state))
            print_board(b)
            if b.check() and b.winner != 0:
                current_player.score += 1
                break
        if current_player is player1:
            current_player = player2
        else:
            current_player = player1


class Population:
    """
    Population class
    """
    _players: List[Player]  # all players in population
    _gen: int = 1  # generation
    _global_best: int  # the best score ever achieved by this population
    _global_best_fitness: int  # the best fitness ever achieved by this population
    _current_best: int  # current best score
    _current_best_player: int  # the position of current best player in the array
    _global_best_player: Player  # a clone of the best player

    def __init__(self, size: int) -> None:
        """
        Constructor

        :param size: size of the population
        """
        self._players = [Player() for i in range(size)]
        self._global_best_player = deepcopy(self._players[0])


if __name__ == "__main__":
    print('Running population as __main__...')
    print('Test play_game function')
    p1 = Player(-1)
    p2 = Player(1)
    n = 1
    np = 100
    j = 0
    players = [Player(0) for i in range(np)]
    for game in range(n):
        for i in range(np):
            for j in range(np):
                ai_play_game(players[i], players[j])
    for player in players:
        print("Player score: %d", player.score)
