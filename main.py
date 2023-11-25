import numpy as np
from sys import argv
from Algorythm import algorythm
from utils import print_list

alreadys_id = []

def treating_input() -> np.ndarray:
    if len(argv) == 1:
        print("Exemple of sliding game :")
        print(np.array([[1, 3, 2],[0, 4, 8],[6, 5, 7]]))
        user_response = input("Type 1 to use a file or type 2 to use the input: ")
        if user_response == "1":
            user_response = input("Type the file name: ")
            with open(user_response, "r") as file:
                lines = file.readlines()
                matrix = np.array([[int(j) for j in i.split()] for i in lines])
                return matrix
        elif user_response == "2":
            user_response = input("Type the size of the sliding puzzle: ")
            size = int(user_response)
            matrix = np.array([[int(input(f"Type the value of the {i}x{j} element: ")) for j in range(size)] for i in range(size)])
            return matrix
    else:
        with open(argv[1], "r") as file:
            lines = file.readlines()
            matrix = np.array([[int(j) for j in i.split()] for i in lines])
            return matrix
    return np.array()

def main():
    starting = treating_input()
    assert all(i in starting for i in range(len(starting)**2)), "Error in the input"
    print_list(algorythm(starting))

if __name__ == "__main__":
    main()