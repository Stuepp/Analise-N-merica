import numpy as np
import math

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matrz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    return np.linalg.solve(A, B)

def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    #exemplo1
    def f(x):
        return  math.exp(-x**2)+math.cos(x)+3
    x0 = 1.7406
    k = 5 # ordem
    n = 15 # número de pontos

    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    x = [1.5198, 1.5504, 1.5869, 1.6172, 1.6485, 1.6654, 1.7106, 1.7257, 1.7605, 1.8094, 1.8469, 1.8675, 1.8925, 1.9451, 1.9771]
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

    print(f'{coeffs = }')
    print(f'{aprox = }')