import numpy as np
import numpy.linalg
import itertools
from scipy.linalg import solve


def basis(A_t):
    b = np.array([20, 50, 90, 1000]).reshape((4, 1))
    try:
        x = solve(A_t, b)
        return x
    except numpy.linalg.LinAlgError:
        return -1


A = np.array(
    [
        [0.3, 0, 0.3, -1, 0, 0],
        [0.1, 0.2, 0.7, 0, -1, 0],
        [0.6, 0.8, 0, 0, 0, -1],
        [1, 1, 1, 0, 0, 0]
    ]
)
b = np.array([20, 50, 90, 1000]).reshape((4, 1))
count = 0
for i in range(0, 5, 1):
    for j in range(i+1, 5, 1):
        print("Curr j: " + str(j) + "\n")
        for k in range(j+1, 5, 1):
            print("Curr k: " + str(k) + "\n")
            for z in range(k+1, 6, 1):
                print("Curr z: " + str(z) + "\n")
                A1 = np.array(
                    [
                        [A[0][i], A[0][j], A[0][k], A[0][z]],
                        [A[1][i], A[1][j], A[1][k], A[1][z]],
                        [A[2][i], A[2][j], A[2][k], A[2][z]],
                        [A[3][i], A[3][j], A[3][k], A[3][z]]
                    ]
                )
                print("Curr A \n")
                print(A1)
                y = basis(A1)
                count += 1
                if y is int and y == -1:
                    print("huy")
                else:
                    print(y, i)
print(count)

my_list = [1,2,3]
list2 = list(itertools.combinations(A[0], 4))
print(list2)
print(len(list2))
print("хуй")
