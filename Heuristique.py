import numpy as np
from settings import HEURISTIC_TYPE

def choose_heuristic(matrix:np.ndarray, SIZE:int, GOAL:np.ndarray) -> int:
    functions = {
        1: manathan_distance,
        2: hamming_distance,
        3: pondered_manathan_distance,
        4: linear_conflict,
    }
    PONDERED = {i + 1: (1 + (i%SIZE == 0) + (i%SIZE == SIZE - 1) + (i < SIZE) + (i > SIZE * SIZE - SIZE)) / 2 for i in range(0, SIZE**2 + 1)}
    return functions[HEURISTIC_TYPE](matrix, SIZE, GOAL, PONDERED)

def hamming_distance(matrix:np.ndarray, SIZE:np.ndarray, GOAL:np.ndarray, PONDERED:np.ndarray) -> int:
    sums = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j] != GOAL[i][j]:
                sums += 1
    return sums * 3

def pondered_manathan_distance(matrix:np.ndarray, SIZE:np.ndarray, GOAL:np.ndarray, PONDERED:np.ndarray) -> int:
    SIZE = len(matrix)
    sums = 0
    for i in range(1, SIZE**2):
        where_1 = np.where(matrix == i)
        where_2 = np.where(GOAL == i)
        sums += PONDERED[i] * (abs(where_1[0][0] - where_2[0][0]) + abs(where_1[1][0] - where_2[1][0]))
    return sums

def manathan_distance(matrix:np.ndarray, SIZE:np.ndarray, GOAL:np.ndarray, PONDERED:np.ndarray) -> int:
        sums = 0
        for i in range(1, SIZE**2):
            where_1 = np.where(matrix == i)
            where_2 = np.where(GOAL == i)
            sums += abs(where_1[0][0] - where_2[0][0]) + abs(where_1[1][0] - where_2[1][0])
        return sums

def linear_conflict(matrix:np.ndarray, SIZE:np.ndarray, GOAL:np.ndarray, PONDERED:np.ndarray) -> int:
    conflict_count = 0
    for i in range(SIZE):
        conflict_count += count_linear_conflict(matrix[i], GOAL[i], SIZE, PONDERED)

        column = [matrix[i][j] for j in range(SIZE)]
        goal_column = [GOAL[i][j] for j in range(SIZE)]
        conflict_count = count_linear_conflict(column, goal_column, SIZE, PONDERED)

def count_linear_conflict(line:np.ndarray, goal_line:np.ndarray, SIZE:np.ndarray, PONDERED:np.ndarray):
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
