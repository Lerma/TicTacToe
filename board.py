from __future__ import annotations

from typing import List


class Board:
    """TicTacToe board"""
    _winner: int
    _game_over: bool
    _state: List[int]

    def __init__(self):
        """
        Simple constructor, return 3x3 board with values set to 0

        """
        self._state = [0] * 9
        self._game_over = False
        self._winner = 0
        print('init successful')

    @property
    def state(self):
        return self._state

    @property
    def winner(self):
        return self._winner

    @property
    def game_over(self):
        return self._game_over

    def move(self, side: int, position: int) -> bool:
        """
        Check if move on `position` is possible, and make it.

        :param side: Player's side (-1 for 'x', 1 for 'o')
        :param position: Chosen position in range 0 to 8
        :return: True if move was successful, False otherwise
        """
        # If position is on the board
        if 0 <= position <= len(self.state):
            # If position is unoccupied
            if self.state[position] == 0:
                # Set player's side to the board on this position
                self.state[position] = side
                # Return True if successful
                if self.check() != 0:
                    self._game_over = True
                return True
            else:
                print('Illegal move! Position is already occupied!')
                return False
        else:
            print('Illegal move! Position is out of the board!')
            return False

    def check(self):
        # convert state to 3x3 matrix
        matrix = []
        for i in range(0, len(self.state), 3):
            matrix.append(self.state[i:i + 3])
        # check rows
        for row in matrix:
            if row == [-1, -1, -1]:
                self._winner = -1
            elif row == [1, 1, 1]:
                self._winner = 1
        # check columns
        for col in list(map(list, zip(*matrix))):
            if col == [-1, -1, -1]:
                self._winner = -1
            elif col == [1, 1, 1]:
                self._winner = 1
        # check diagonals
        if [matrix[i][i] for i in range(3)] == [-1, -1, -1] or [matrix[3 - 1 - i][i] for i in range(3)] == [-1, -1, -1]:
            self._winner = -1
        elif [matrix[i][i] for i in range(3)] == [1, 1, 1] or [matrix[3 - 1 - i][i] for i in range(3)] == [1, 1, 1]:
            self._winner = 1
        # check for draw
        if all(pos != 0 for pos in self.state) and self.winner == 0:
            self._game_over = True
            print('Draw!')
            return self.game_over
        if self.winner == -1:
            self._game_over = True
            print('x won!')
        elif self.winner == 1:
            self._game_over = True
            print('o won!')
        return self.game_over


def print_board(board: Board):
    """
    Prints board state to console

    :param board:
    """
    # first replace list with 'x' and 'o'
    l = ['x' if el == -1 else 'o' if el == 1 else '_' for el in board.state]
    # then split list by 3 and print it
    print('Board:')
    for i in range(0, len(l), 3):
        print(*l[i:i + 3])


if __name__ == "__main__":
    print('Running board module as __main__...')
    b = Board()
    print_board(b)
    b.move(-1, 2)
    print_board(b)
    b.move(1, 1)
    b.move(-1, 4)
    b.move(1, 0)
    b.move(-1, 0)
    b.move(-1, -1)
    print_board(b)
    b.move(-1, 6)
    print_board(b)
