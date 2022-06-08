import numpy as np
import math

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a*x*math.e**(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.5275, 1.2798, 1.8354, 2.995, 3.5563, 4.8647, 5.7268, 6.186, 6.9649, 7.8094, 8.3545, 9.779]
    y = [1.5421, 2.7825, 3.1861, 3.3406, 3.1962, 2.6972, 2.2813, 2.0573, 1.7578, 1.4752, 1.2498, 0.8957]
    x_ = x # pode mudar com a func
    y_ = np.log(np.divide(y,x)) # pode mudar com a func

    grau = 1 # pode mudar com a func

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = math.e**a1 # pode mudar com a func
    b = a0 # pode mudar com a func

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    x_values = [2.903, 7.0083, 8.3974]
    
    for xi_v in x_values:
        print(p(xi_v))