import numpy as np
from Taquin import Taquin
from global_variable import HEURISTIC_TYPE, SIZE

def get_id(matrix:np.ndarray) -> int:
    return hash(str(matrix))

def print_list(taquins:list):
    print("List of effectued moves :\n")
    for i in range(0, len(taquins), 10):
        for j in range(len(taquins[i].matrix)):
            for k in range(i, min(i + 10, len(taquins))):
                print(taquins[k].matrix[j], end=" ")
            print()
        if i + 10 < len(taquins):
            print('\n')

def add_new_taquin(to_treat:list, matrix:np.ndarray, current:object) -> list:
    new_taquin = Taquin(current.previous_distance + 1, current.previous + [current], matrix)
    to_treat.append(new_taquin)
    return to_treat
