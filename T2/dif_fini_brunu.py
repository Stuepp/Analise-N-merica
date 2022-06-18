import numpy as np
import math

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1]* n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matriz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    return np.linalg.solve(A, B)

def dif_fin(coeffs,y):
    return sum(ci * yi for ci, yi in zip (coeffs, y))
if __name__ == '__main__':

    #exemplo 1
    def f(x):
        return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)
    x0 = 2.912
    k = 4
    n = 8 # numero de pontos 

    # queremos pontos no intervalo [x0 - e, x0 + e]
    x = [2.7206, 2.7339, 2.8462, 2.8836, 2.9193, 2.9821, 3.0767, 3.111]
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)
    
    print (f'{coeffs = }')
    print (f'{aprox = }')