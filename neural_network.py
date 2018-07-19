import random

import matrix


class NeuralNetwork:
    """A general neural network class"""

    def __init__(self, i_nodes, h_nodes, o_nodes):
        # set neural network size
        self._i_nodes = i_nodes
        self._h_nodes = h_nodes
        self._o_nodes = o_nodes
        # create first (input --> hidden) layer weights (including bias) (rows -> neutrons, columns -> synapses)
        self._wih = None
        self.wih = [[random.uniform(0, 1) for col in range(self._h_nodes + 1)] for row in range(self._i_nodes)]
        # same for second (hidden -> output) layer
        self._who = None
        self.who = [[random.uniform(0, 1) for col in range(self._o_nodes + 1)] for row in range(self._h_nodes)]

    def mutate(self, mr):
        """Mutation function for genetic algorithm"""
        self.wih = matrix.mutate(self.wih, mr)
        self.who = matrix.mutate(self.who, mr)

    def output(self, nn_input):
        """Calculate network output"""
        # convert input to matrix
        inputs = [[el] for el in nn_input]
        # add bias
        inputs_bias = matrix.add_bias(inputs)
        # calculate output
        # apply layer one weights to the inputs
        h_input = matrix.dot(self.wih, inputs_bias)
        # activate input layer
        h_output = matrix.activation(h_input)
        # add bias
        hidden_bias = matrix.add_bias(h_output)
        # apply layer two weights
        o_input = matrix.dot(self.who, hidden_bias)
        # activate hidden layer
        o_output = matrix.activation(o_input)
        output = o_output
        return output

    def crossover(self, partner):
        child = NeuralNetwork(self._i_nodes, self._h_nodes, self._o_nodes)
        child.wih = matrix.crossover(self.wih, partner.wih)
        child.who = matrix.crossover(self.who, partner.who)
        return child

    @property
    def wih(self):
        """Weights between input layer and hidden layer"""
        return self._wih

    @wih.setter
    def wih(self, weights):
        self._wih = weights

    @property
    def who(self):
        """Weights between hidden layer and output layer"""
        return self._who

    @who.setter
    def who(self, weights):
        self._who = weights


n = NeuralNetwork(2, 2, 2)
matrix.print_matrix(n.wih)
print('')
matrix.print_matrix(n.who)
print('')
n_input = [1, -1]
out = n.output(n_input)
print(out)
