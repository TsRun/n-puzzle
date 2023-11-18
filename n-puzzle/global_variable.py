import numpy as np

HEURISTIC_TYPE = int(input("Choose heuristic:\n1. Manhattan\n2. Hamming\n3. Euclidean\n4. Linear Conflict\n5. Manhattan + Linear Conflict\n6. Hamming + Linear Conflict\n7. Euclidean + Linear Conflict\n8. Manhattan + Hamming + Linear Conflict\n9. Manhattan + Euclidean + Linear Conflict\n10. Hamming + Euclidean + Linear Conflict\n11. Manhattan + Hamming + Euclidean + Linear Conflict\n"))
SIZE = 4
GOAL = np.array([[i * SIZE + j + 1 if i != SIZE - 1 or j != SIZE - 1 else 0 for j in range(SIZE)] for i in range(SIZE)])
