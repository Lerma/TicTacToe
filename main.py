from board import Board
from player import Network

print('Hello world!')
b = Board()
n = Network(1)
n.save('weights.txt')
n.load('weights.txt')
s = -1
pos = []
while True:
    b.show()
    print("Current move is %s " % ('x' if s == -1 else 'o',))
    if s == -1:
        pos = input("Enter position:")
        pos = pos.split()
        pos = list(map(int, pos))
        pos = [x - 1 for x in pos]
    else:
        print('AI turn')
        values = [item for row in b.state for item in row]
        n.init_input(values)
        idx = n.calculate()
        pos[0] = idx // 3
        pos[1] = idx % 3
    # Make move
    b.move(s, pos)
    # Change side
    s = -s
    # Check win condition
    if b.check() != 0:
        b.show()
        break
