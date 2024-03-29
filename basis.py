import numpy as np
import numpy.linalg
from scipy.linalg import solve


def basis(A_t):
    b = np.array([20, 50, 90, 1000]).reshape((4, 1))
    try:
        x = solve(A_t, b)
        return x
    except numpy.linalg.LinAlgError:
        return -1


def add_zero(y_old, a, b, c, d):
    y_t = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]).reshape((6, 1))
    y_t[a] = y_old[0]
    y_t[b] = y_old[1]
    y_t[c] = y_old[2]
    y_t[d] = y_old[3]
    return y_t


def make_Lk(n, a, b, c, d):
    k = 0
    Lk = np.array([0, 0]).reshape((2, 1))
    for count in range(0, 6, 1):
        if count != a and count != b and count != c and count != d:
            Lk[k] = count + 1
            k += 1
    print("Lk = ")
    print(Lk)
    return Lk


def constr_dK(y_t, c_t, a, b, c, d, A1_t, A_t):
    Nk = np.array([a + 1, b + 1, c + 1, d + 1]).reshape((4, 1))
    print(Nk)
    print("\n")
    Lk = make_Lk(2, a, b, c, d)
    B_t = np.linalg.inv(A1_t)
    print("\n" + "B =")
    print(B_t)
    k1 = 0
    c_t_Nk = np.array([0.0, 0.0, 0.0, 0.0]).reshape((4, 1))
    for cou_c in Nk:
        c_t_Nk[k1] = c_t[cou_c - 1]
        k1 += 1
    y_d = B_t.dot(c_t_Nk)
    print("\n" + "y_d =")
    print(y_d)
    A_Lk = np.array(
        [
            [0.0, 0.0],
            [0.0, 0.0],
            [0.0, 0.0],
            [0.0, 0.0]
        ]
    )
    for cou_A_m in range(0, 4, 1):
        k_A = 0
        for cou_A in Lk:
            A_Lk[cou_A_m, k_A] = A_t[cou_A_m, cou_A - 1]
            k_A += 1
    print("\n" + "A_Lk =")
    print(A_Lk)
    k_c_Lk = 0
    c_t_Lk = np.array([0.0, 0.0]).reshape((2, 1))
    for cou_c_Lk in Lk:
        c_t_Lk[k_c_Lk] = c_t[cou_c_Lk - 1]
        k_c_Lk += 1
    print("\n" + "c_Nk =")
    print(c_t_Nk)
    print("\n" + "c_Lk =")
    print(c_t_Lk)
    prom = B_t.dot(A_Lk)
    dk = c_t_Lk.T - np.dot(c_t_Nk.T, prom)
    print("\n" + "dk = ")
    print(dk)
    return dk


def check_dk(dk):
    for cou in range(0, 2, 1):
        if dk[0][cou] < 0:
            return 0
        else:
            return 1


def search_dk(dk):
    for cou in range(0, 2, 1):
        if dk[0][cou] < 0:
            return cou


A = np.array(
    [
        [0.3, 0, 0.3, -1, 0, 0],
        [0.1, 0.2, 0.7, 0, -1, 0],
        [0.6, 0.8, 0, 0, 0, -1],
        [1, 1, 1, 0, 0, 0]
    ]
)
b = np.array([20, 50, 90, 1000]).reshape((4, 1))
c = np.array([30, 15, 20, 0, 0, 0]).reshape((6, 1))
count = 0
print(A.T)
for i in range(0, 5, 1):
    for j in range(i + 1, 5, 1):
        for k in range(j + 1, 5, 1):
            for z in range(k + 1, 6, 1):
                A1 = np.array(
                    [
                        [A[0][i], A[0][j], A[0][k], A[0][z]],
                        [A[1][i], A[1][j], A[1][k], A[1][z]],
                        [A[2][i], A[2][j], A[2][k], A[2][z]],
                        [A[3][i], A[3][j], A[3][k], A[3][z]]
                    ]
                )
                y = basis(A1)
                count += 1
                if isinstance(y, int) and y == -1:
                    print("")
                else:
                    err = 0
                    for cou in range(0, 4, 1):
                        if y[cou][0] < 0:
                            err = +1
                    if err == 0:
                        print("Curr A \n")
                        print(A1)
                        print("\n" + "i = " + str(i) + " j = " + str(j) + " k = " + str(k) + " z = " + str(z) + "\n")
                        print(y)
                        y_new = add_zero(y, i, j, k, z)
                        print("\n" + "y_new = ")
                        print(y_new)
                        print("\n")

                        dK = constr_dK(y_new, c, i, j, k, z, A1, A)
                        Lk = make_Lk(2, i, j, k, z)
                        #while check_dk(dK) == 0:
                         #   A_j = np.array(
                          #      [
                           #         A[0][search_dk(dK)],
                            #        A[1][search_dk(dK)],
                             #       A[2][search_dk(dK)],
                              #      A[3][search_dk(dK)]
                               # ]
                            #)
                            #uk = np.linalg.inv(A1).dot(A_j)
                            #print("\nuk = ")
                            #print(uk)
                        if check_dk(dK) == 1:
                            print("Оптимальное решение: " + "\n")
                            print(y_new)
                            z = 6
                            k = 5
                            j = 5
                            i = 5
                            break
