from __future__ import annotations

import random
from copy import deepcopy
from typing import List

from board import Board
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
    _current_best_player: Player  # the position of current best player in the array
    _global_best_player: Player  # a clone of the best player

    def __init__(self, size: int, mutation_rate: float = 0.2) -> None:
        """
        Constructor

        :param size: size of the population
        """
        self._mutation_rate = mutation_rate
        self._players = [Player() for i in range(size)]
        self._gen = 1
        self._current_best_player = deepcopy(self._players[0])
        self._global_best_player = deepcopy(self._players[0])

    @property
    def current_best_player(self) -> Player:
        """
        Best player in this generation

        :return: Player
        """
        return self._current_best_player

    @property
    def global_best_player(self) -> Player:
        """
        Best player in the population

        :return: Player
        """
        return self._global_best_player

    @property
    def gen(self) -> int:
        """
        Current generation

        :return:
        """
        return self._gen

    def select_best_players(self, player_num: int) -> List[Player]:
        """
        Returns ``player_num`` best players in population based on ``player.score``.
        If there is less players in the population, than requested, returns all of them.

        :param player_num:
        :return:
        """
        if player_num > len(self._players) - 1:
            player_num = len(self._players) - 1
        out = sorted(self._players, key=lambda x: x.score)
        return out[0:player_num]

    def set_best_player(self):
        """
        Set current_best_player and global_best_player (if current best player is better than global best player)

        """
        self._current_best_player = self.select_best_players(1)[0]
        if self.current_best_player.score > self.global_best_player.score:
            self._global_best_player = self.current_best_player

    def train_population(self):
        for player in self._players:
            for opponent in self._players:
                ai_play_game(player, opponent)

    def next_generation(self):
        """
        Natural selection of players based on player's score

        """
        # first set current and global best players
        self.set_best_player()
        # create empty list for new generation
        children = []
        # choose two parents randomly with respect to their score
        parents_1 = random.choices(population=self._players, weights=[player.score for player in self._players],
                                   k=len(self._players))
        parents_2 = random.choices(population=self._players, weights=[player.score for player in self._players],
                                   k=len(self._players))
        # and crossover them
        for par_1, par_2 in zip(parents_1, parents_2):
            children.append(par_1.crossover(par_2))
        # mutate children
        for child in children:
            child.mutate(self._mutation_rate)
        # replace old players with new players
        self._players = deepcopy(children)
        self._gen += 1


if __name__ == "__main__":
    print('Running population as __main__...')
    population = Population(20)
    for i in range(100):
        population.train_population()
        print("Generation = %d, global best player score = %d, current best player score = %d" % (
        population.gen, population.global_best_player.score, population.current_best_player.score))
        population.next_generation()
    population.global_best_player.save("trained3")
