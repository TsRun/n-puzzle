import numpy as np
from Taquin import Taquin
import settings

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

def add_new_taquin(to_treat:list, matrix:np.ndarray, current:object, SIZE:int, GOAL:np.ndarray) -> list:
    new_taquin = Taquin(current.previous_distance + 1, current.previous + [current], matrix, SIZE, GOAL)
    to_treat.append(new_taquin)
    return to_treat

def count_inversions(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j] and arr[i] != 0 and arr[j] != 0:
                inv_count += 1
    return inv_count

def is_solvable(puzzle):
    # Aplatir le puzzle et compter les inversions
    flattened_puzzle = puzzle.flatten()
    inversions = count_inversions(flattened_puzzle)

    # Vérifier la taille de la grille
    size = puzzle.shape[0]
    if size % 2 != 0:
        # Pour les grilles impaires, le nombre d'inversions doit être pair
        return inversions % 2 == 0
    else:
        # Pour les grilles paires, vérifier la parité de la rangée de la case vide et du nombre d'inversions
        row_from_bottom = size - np.where(puzzle == 0)[0][0]
        return (row_from_bottom % 2 != 0) == (inversions % 2 == 0)
