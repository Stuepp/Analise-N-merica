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
    return a * 2 **(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x =  [0.0025, 0.0821, 0.1409, 0.2059, 0.2514, 0.2854, 0.3868, 0.4233, 0.4908, 0.5162, 0.5715, 0.616, 0.7111, 0.7228, 0.8187, 0.8797, 0.9225, 0.9885, 1.0357, 1.0661, 1.1203, 1.1953, 1.2602, 1.3106, 1.3793, 1.4026, 1.4588, 1.5212, 1.5808, 1.6189, 1.6676, 1.7592, 1.8232, 1.8581, 1.9378, 1.9736]
    y = [5.2613, 5.0312, 6.0904, 9.114, 6.6619, 4.1697, 7.9473, 9.9611, 8.2309, 8.5234, 9.3869, 9.9668, 10.3235, 10.435, 11.7769, 14.2749, 14.3107, 15.6144, 16.2445, 17.3347, 20.4939, 21.639, 20.8813, 23.5755, 23.2161, 26.5316, 26.8637, 30.2521, 32.2191, 34.9046, 35.8954, 39.6029, 42.8255, 44.9333, 48.8092, 51.3153]
    x_ = x
    y_ = np.log(y) # pode mudar com a func

    grau = 1 # pode mudar com a func

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    b = a1/np.log(2) # pode mudar com a func
    a = math.e**a0 # pode mudar com a func

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    x_values = [0.6238, 0.7112, 1.2497, 1.537, 1.7143]
    
    for xi_v in x_values:
        print(p(xi_v))