import random

import ai
import board


def error(train_set):
    """Error calculated by MSE function
    Args:
        train_set (list): Nested list in form
            [
                [(n1a1, n1i1),(n2a1, n2i1),(n3a1, n3i1)],
                [(n1a2, n1i2),(n2a2, n2i2),(n3a3, n3i3)]
            ]
            where n - neuron, a - network output, i - ideal output

    Returns:
        list: List of errors for neurons
    """
    err = []
    inv = map(list, zip(*train_set))
    for i, neuron in enumerate(inv):
        err.append(0)
        for res in neuron:
            err[i] += (res[0] - res[1]) ** 2 / len(train_set)
    return err


def random_board(n):
    b = board.Board()
    s = -1
    i = 1
    while i <= n:
        rnd = random.randint(0, 8)
        pos = [rnd // 3, rnd % 3]
        m = b.move(s, pos)
        if m == 0:
            s = -s
            i += 1
    return b


def teach():
    b = board.Board()
    n = ai.Network()
    n.load('weights.txt')
    s = -1
    pos = []
    while pos != [0]:
        values = [item for row in b.state for item in row]
        n.init_input(values)
        idx = n.calculate()
        print('AI move: %d %d' % (idx // 3, idx % 3))
        b.move(s, [idx // 3, idx % 3])
        b.show()
        if b.check() != 0:
            break
        expect = input('Enter expected move:')
        s = -s
        pos = input('Player move:')
        pos = pos.split()
        pos = list(map(int, pos))
        pos = [x - 1 for x in pos]
        b.move(s, pos)
        b.show()
        if b.check() != 0:
            break
