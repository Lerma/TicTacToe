import pickle

from neural_network import NeuralNetwork


class Player:
    _is_training: bool
    _brain: NeuralNetwork
    _side: int
    _score: int
    _filename: str

    def __init__(self, side: int = -1):
        self._side = side
        self._score = None
        self.score = 0
        self._brain = NeuralNetwork(9, 9, 9)
        self._is_training = None
        self.is_training = False
        self._filename = 'player1'

    @property
    def brain(self) -> NeuralNetwork:
        return self._brain

    @property
    def score(self) -> int:
        """
        Number of games won by this player
        """
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def is_training(self) -> bool:
        return self._is_training

    @is_training.setter
    def is_training(self, is_training: bool):
        self._is_training = is_training

    @property
    def filename(self) -> str:
        """
        Name of the file containing player's brains
        """
        return self._filename

    @filename.setter
    def filename(self, filename: str):
        self._filename = filename

    @property
    def side(self) -> int:
        """
        Player's side (-1 for 'x', 1 for 'o')
        """
        return self._side

    @side.setter
    def side(self, side: int):
        self._side = side

    def mutate(self, mr: int):
        """
        Mutate player's brain

        :param mr: rate
        """
        self.brain.mutate(mr)

    def save(self, filename: str = None):
        """
        Save player's brains to file (by pickling them)

        :param filename: String with file name
        """
        if not filename:
            filename = self.filename
        with open(filename, 'wb') as f:
            pickle.dump(self.brain, f)

    def load(self, filename: str = None):
        """
        Load player's brains from file

        :param filename: String with file name
        """
        if not filename:
            filename = self.filename
        with open(filename, 'rb') as f:
            self._brain = pickle.load(f)

    def make_move(self, board: list) -> int:
        """
        Calculate neural network output and choose best unoccupied position for the next move

        :param board: Current board state
        :return: Position on the board
        """
        output = self.brain.output(board)
        out = []
        for i, j in zip(board, output):
            if i is 0:
                out.append(j)
            else:
                out.append(0)
        print("Player decision is %s" % str(out))
        position = out.index(max(out))
        return position


if __name__ == "__main__":
    test_board = [1, -1, 1, 0, 1, 0, -1, 0, 0]
    player = Player(-1)
    print(player.make_move(test_board))
    player.save('player')
    player2 = Player(-1)
    player2.load('player')
    print(player2.make_move(test_board))
    print(str(player2.brain.wih == player.brain.wih))
