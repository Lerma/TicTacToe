from __future__ import annotations

from copy import deepcopy
from typing import List

from player import Player


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

    def calc_fitness(self):
