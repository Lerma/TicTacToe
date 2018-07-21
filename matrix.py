import copy
import math
import random
from typing import List


def sigmoid(x: float) -> float:
    """
    Sigmoid function
    """
    return 1 / (1 + math.exp(-x))


def der_sigmoid(x: float) -> float:
    """
    Sigmoid function derivative
    """
    return x * (1 - x)


def activation(matrix: List[List[float]]) -> List[List[float]]:
    """
    Activation matrix
    """
    out = copy.deepcopy(matrix)
    for i, row in enumerate(out):
        for j, el in enumerate(row):
            out[i][j] = sigmoid(el)
    return out


def der_activation(matrix: List[List[float]]) -> List[List[float]]:
    """
    Derived activation matrix
    """
    out = copy.deepcopy(matrix)
    for i, row in enumerate(out):
        for j, el in enumerate(row):
            out[i][j] = der_sigmoid(el)
    return out


def add_bias(matrix: List[List[float]]) -> List[List[float]]:
    """
    Adds one row with elements set to 1
    """
    out = copy.deepcopy(matrix)
    out.append([1 for i in range(len(matrix[0]))])
    return out


def mutate(matrix: List[List[float]], rate: float) -> List[List[float]]:
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


def crossover(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    """Returns a matrix, which has a random number of values from matrix1 and the rest from matrix2"""
    out = copy.deepcopy(matrix1)
    # pick a random point in the matrix
    (r, c) = (random.randrange(len(matrix1)), random.randrange(len(matrix1[0])))
    for i in range(r, len(matrix1)):
        for j in range(len(matrix1[0])):
            if j >= c or i > r:
                out[i][j] = matrix2[i][j]
    return out


def print_matrix(matrix: List[List[float]]):
    """line by line matrix print"""
    for row in matrix:
        print(' '.join(map(str, row)))
    print('')


def dot(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    """Dot product of matrix1 and matrix 2"""
    out = [[None for col in matrix2[0]] for row in matrix1]
    if len(matrix1[0]) == len(matrix2):
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                s = 0
                for k in range(len(matrix2)):
                    s += matrix1[i][k] * matrix2[k][j]
                out[i][j] = s
    return out


def col_to_row(matrix: List[List[float]]) -> List[float]:
    return [el for row in matrix for el in row]


if __name__ == "__main__":
    print('Running matrix module as __main__...')
    mat = [[random.randint(0, 5) for el in range(3)] for row in range(3)]
    col = [[random.randint(0, 5)] for i in range(4)]
    row = [[random.randint(0, 5) for i in range(3)]]
    print('matrix 1 is:')
    print_matrix(mat)
    print('col is:')
    print_matrix(col)
    a = activation(mat)
    print_matrix(a)
    b = add_bias(mat)
    print_matrix(b)
    m = mutate(activation(mat), 0.5)
    print_matrix(m)
    mat2 = [[random.randint(0, 5) for el in range(3)] for i in range(3)]
    c = crossover(mat, mat2)
    print_matrix(c)
    d = dot(row, mat2)
    print_matrix(d)
    print(col_to_row(col))
