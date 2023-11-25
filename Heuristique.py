import numpy as np
from global_variable import HEURISTIC_TYPE, SIZE, GOAL

PONDERED = {a:1 + (a%SIZE == 1) + (a%SIZE == 0) + (a <= SIZE) + (a > SIZE * (SIZE - 1)) for a in range(1, SIZE**2)}

def choose_heuristic(matrix:np.ndarray) -> int:
    if HEURISTIC_TYPE == 1:
        return manathan_distance(matrix)
    elif HEURISTIC_TYPE == 2:
        return hamming_distance(matrix)
    elif HEURISTIC_TYPE == 3:
        return pondered_manathan_distance(matrix)
    elif HEURISTIC_TYPE == 4:
        return linear_conflict(matrix)

def hamming_distance(matrix:np.ndarray) -> int:
    return np.sum(matrix != GOAL)

def pondered_manathan_distance(matrix:np.ndarray) -> int:
    SIZE = len(matrix)
    sums = 0
    for i in range(1, SIZE**2):
        where_1 = np.where(matrix == i)
        where_2 = np.where(GOAL == i)
        sums += PONDERED[i] * (abs(where_1[0][0] - where_2[0][0]) + abs(where_1[1][0] - where_2[1][0]))
    return sums

def manathan_distance(matrix:np.ndarray) -> int:
        sums = 0
        for i in range(1, SIZE**2):
            where_1 = np.where(matrix == i)
            where_2 = np.where(GOAL == i)
            sums += abs(where_1[0][0] - where_2[0][0]) + abs(where_1[1][0] - where_2[1][0])
        return sums

def linear_conflict(matrix:np.ndarray) -> int:
    conflict_count = 0
    for i in range(SIZE):
        conflict_count += count_linear_conflict(matrix[i], GOAL[i])

        column = [matrix[i][j] for j in range(SIZE)]
        goal_column = [GOAL[i][j] for j in range(SIZE)]
        conflict_count = count_linear_conflict(column, goal_column)

def count_linear_conflict(line, goal_line):
    conflicts = 0
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if (
                line[i] != 0 and line[j] != 0 and
                goal_line.index(line[i]) > goal_line.index(line[j]) and
                PONDERED[line[i]] + PONDERED[line[j]] > 2
            ):
                conflicts += 1
    return conflicts
