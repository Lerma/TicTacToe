import copy
import math
import random


def sigmoid(x):
    """Sigmoid function"""
    return 1 / (1 + math.exp(-x))


def der_sigmoid(x):
    """Sigmoid derivative"""
    return x * (1 - x)


def activation(matrix):
    """Activation matrix"""
    out = copy.deepcopy(matrix)
    for i, row in enumerate(out):
        for j, el in enumerate(row):
            out[i][j] = sigmoid(el)
    return out


def der_activation(matrix):
    """Derived activation matrix"""
    out = copy.deepcopy(matrix)
    for i, row in enumerate(out):
        for j, el in enumerate(row):
            out[i][j] = der_sigmoid(el)


def add_bias(matrix):
    """Adds one row with elements set to 1"""
    out = copy.deepcopy(matrix)
    out.append([1 for i in range(len(matrix[0]))])
    return out


def mutate(matrix, rate):
    """Mutation function for genetic algorithm"""
    out = copy.deepcopy(matrix)
    # if chosen to be mutated
    if random.random() < rate:
        for i, row in enumerate(out):
            for j, el in enumerate(row):
                out[i][j] += random.gauss(0, 0.2)
                if out[i][j] > 1:
                    out[i][j] = 1
                if out[i][j] < -1:
                    out[i][j] = -1
    return out


def crossover(matrix1, matrix2):
    """Returns a matrix, which has a random number of values from matrix1 and the rest from matrix2"""
    out = copy.deepcopy(matrix1)
    # pick a random point in the matrix
    (r, c) = (random.randrange(len(matrix1)), random.randrange(len(matrix1[0])))
    for i in range(r, len(matrix1)):
        for j in range(len(matrix1[0])):
            if j >= c or i > r:
                out[i][j] = matrix2[i][j]
    return out


def print_matrix(matrix):
    """line by line matrix print"""
    for row in matrix:
        print(' '.join(map(str, row)))


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = activation(mat)
print_matrix(a)
print('')
b = add_bias(mat)
print_matrix(b)
print('')
m = mutate(activation(mat), 0.5)
print_matrix(m)
print('')
mat2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
c = crossover(mat, mat2)
print_matrix(c)
