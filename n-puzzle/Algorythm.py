import numpy as np
from Taquin import Taquin
from utils import get_id, add_new_taquin
from global_variable import SIZE


def algorythm(starting:np.ndarray) -> list:
    starting = Taquin(0, [], starting)
    alreadys = [starting.id]
    to_treat = [starting]
    print(starting)
    while True:
        to_treat.sort(key=lambda x: x.sum)
        current = to_treat.pop(0)
        alreadys.append(current.id)
        if current.heuristic == 0:
            return current.previous
        for move in current.get_possible_moves():
            new_matrix = current.after_move(move)
            new_id = get_id(new_matrix)
            if new_id not in alreadys:
                if new_id in [i.id for i in to_treat]:
                    for i in to_treat:
                        if i.id == new_id:
                            if i.previous_distance > current.previous_distance + 1:
                                to_treat.remove(i)
                                to_treat = add_new_taquin(to_treat, new_matrix, current)
                else:
                    to_treat = add_new_taquin(to_treat, new_matrix, current)
