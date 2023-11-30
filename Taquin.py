import numpy as np
from Heuristique import choose_heuristic

class Taquin:
    """
    Taquin class
    """

    def __init__(self, previous_distance:int, previous:list, matrix:np.ndarray, SIZE:int, GOAL:np.ndarray):
        self.matrix = matrix
        self.previous_distance = previous_distance
        self.previous = previous
        self.heuristic = self.calcul_heuristic(SIZE, GOAL)
        self.sum = self.heuristic + self.previous_distance
        self.id = hash(str(matrix))

    def __str__(self):
        return str(self.matrix) + '\n'

    def __repr__(self):
        return str(self.matrix)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Taquin):
            return self.id == other.id
        else:
            return super().__eq__(other)

    def calcul_heuristic(self, SIZE:int, GOAL:np.ndarray) -> int:
        return choose_heuristic(self.matrix, SIZE, GOAL)

    def get_possible_moves(self, SIZE:int) -> list:
        """
        Get the possible moves from the current state
        """
        moves = []
        for i in range(SIZE):
            for j in range(SIZE):
                if self.matrix[i][j] == 0:
                    if i > 0:
                        moves.append((i - 1, j))
                    if i < SIZE - 1:
                        moves.append((i + 1, j))
                    if j > 0:
                        moves.append((i, j - 1))
                    if j < SIZE - 1:
                        moves.append((i, j + 1))
        return moves

    def after_move(self, move:tuple) -> np.ndarray:
        """
        Return a new matrix after a move
        """
        new_matrix = np.copy(self.matrix)
        new_matrix[move[0]][move[1]], new_matrix[self.matrix == 0] = new_matrix[self.matrix == 0], new_matrix[move[0]][move[1]]
        return new_matrix


