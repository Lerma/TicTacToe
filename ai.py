import math
from ast import literal_eval
from random import uniform


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


class InputNeuron:
    def __init__(self, num, val):
        self.value = val
        self.num = num


class HiddenNeuron:
    def __init__(self, num, input_layer):
        self.w = [uniform(-1, 1) for n in input_layer]
        self.num = num
        self.value = 0

    def evaluate(self, input_layer):
        val = 0
        for idx, n in enumerate(input_layer):
            val += n.value * self.w[idx]
        self.value = sigmoid(val)


class OutputNeuron:
    def __init__(self, num, hidden_layer):
        self.w = [uniform(-1, 1) for n in hidden_layer]
        self.num = num
        self.value = 0

    def evaluate(self, hidden_layer):
        val = 0
        for idx, n in enumerate(hidden_layer):
            val += n.value * self.w[idx]
        self.value = sigmoid(val)


class Network:
    def __init__(self, side):
        self.input_layer = [InputNeuron(i, 0) for i in range(9)]
        self.hidden_layer = [HiddenNeuron(i, self.input_layer) for i in range(3)]
        self.output_layer = [OutputNeuron(i, self.hidden_layer) for i in range(9)]
        self.decision = 0
        self.side = side
        self.err = 0

    def init_input(self, values):
        for idx, n in enumerate(self.input_layer):
            n.value = values[idx]

    def calculate(self):
        lst = []
        for n in self.hidden_layer:
            n.evaluate(self.input_layer)
        for n in self.output_layer:
            n.evaluate(self.hidden_layer)
            lst.append(n.value)
        out = [x if self.input_layer[idx].value == 0 else 0 for idx, x in enumerate(lst)]
        print('AI decision:')
        print(out)
        if self.side == 1:
            self.decision = lst.index(max(out))
        else:
            self.decision = lst.index(min(out))
        print(self.decision)
        return self.decision

    def save(self, filename):
        with open(filename, 'w') as file:
            for n in self.hidden_layer:
                file.write(str(n.w) + '\n')
            for n in self.output_layer:
                file.write(str(n.w) + '\n')

    def load(self, filename):
        with open(filename, 'r') as file:
            print('Reading weights from file...')
            print('Hidden layer:')
            for n in self.hidden_layer:
                n.w = literal_eval(file.readline())
                print(n.w)
            print('Output layer:')
            for n in self.output_layer:
                n.w = literal_eval(file.readline())
                print(n.w)

    def mse(self, decision, right_move):
        self.err = 0
        for i in range(len(decision)):
            self.err += (decision[i] - right_move[i]) ** 2
        self.err = self.err / len(decision)
        return self.err

    def teach(self, values, right_move):
        self.init_input(values)
        decision = self.calculate()
        error = self.mse(decision, right_move)
        der = (1 - decision) * decision
        delta_out = (right_move - decision) * der
        delta_hidden = der * sum()
