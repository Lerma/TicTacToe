class Board:
    """Class of TicTacToe board"""
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    is_ended = False
    winner = 0

    def __init__(self):
        self.state = [[0 for i in range(3)] for j in range(3)]
        self.is_ended = False
        self.winner = 0

    def show(self):
        print('Board:')
        for row in self.state:
            print(*['x' if i == -1 else 'o' if i == 1 else '_' for i in row])

    def move(self, side, position):
        if 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
            if self.state[position[0]][position[1]] == 0:
                self.state[position[0]][position[1]] = side
                return 0
            else:
                print('Illegal move! Slot is already occupied!')
        else:
            print('Illegal move! Out of the board!')
            return 1

    def check(self):
        # check rows
        for row in self.state:
            if row == [-1, -1, -1]:
                self.winner = -1
            elif row == [1, 1, 1]:
                self.winner = 1
        # check columns
        for col in list(map(list, zip(*self.state))):
            if col == [-1, -1, -1]:
                self.winner = -1
            elif col == [1, 1, 1]:
                self.winner = 1
        # check diagonals
        if [self.state[i][i] for i in range(3)] == [-1, -1, -1] or [self.state[3 - 1 - i][i] for i in range(3)] == [-1,
                                                                                                                    -1,
                                                                                                                    -1]:
            self.winner = -1
        elif [self.state[i][i] for i in range(3)] == [1, 1, 1] or [self.state[3 - 1 - i][i] for i in range(3)] == [1, 1,
                                                                                                                   1]:
            self.winner = 1
        if self.winner == -1:
            print('x won!')
        elif self.winner == 1:
            print('o won!')
        return self.winner
