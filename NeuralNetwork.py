import random
import matrix
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
        self._wih = [[random.uniform(0, 1) for i in range(self._h_nodes)] for j in range(self._i_nodes + 1)]
        # same for second (hidden -> output) layer
        self._who = [[random.uniform(0, 1) for i in range(self._o_nodes)] for j in range(self._h_nodes + 1)]

    def mutate(self, mr):
        """Mutation function for genetic algorithm"""
        self._wih = matrix.mutate(self._wih, mr)
        self._who = matrix.mutate(self._who, mr)

    def output(self, input):
        """Calculate network output"""
        # convert input to matrix

        return output

    def activation(self):


class Neuron:
    """A general neuron class"""

    def __init__(self, i_nodes, h_nodes, o_nodes):
        self._i_nodes = i_nodes


class Synapse:
    """A general synapse class"""

    def __init__(self, weight):
        self._w = weight

    @property
    def w(self):
        """Wight of the synapse"""
        return self._w

    @w.setter
    def w(self, weight):
        self._w = weight

    @w.deleter
    def w(self):
        del self._w


n = NeuralNetwork(9, 9, 9)
