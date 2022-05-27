import numpy as np
# import scipy as sp

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

x = [0.2831, 0.5994, 0.8724, 0.9699, 1.4108, 1.6902, 2.236, 2.5542, 2.7035, 2.9099, 3.4123, 3.6344, 4.0147, 4.2914, 4.8225, 4.9961, 5.2596, 5.618, 6.0346, 6.1457, 6.715, 6.9093, 7.3299, 7.4711, 7.797, 8.1503, 8.6575, 8.7201, 9.1815, 9.5179, 9.7272]
y = [6.1598, 5.5278, 5.4797, 5.2002, 5.1956, 4.8627, 4.2425, 5.1528, 4.0793, 3.8612, 3.877, 3.3907, 3.6204, 3.2685, 5.0082, 3.2496, 3.2299, 3.3571, 3.0023, 3.155, 3.3467, 3.1391, 3.4408, 3.7133, 4.6364, 3.9276, 4.1531, 4.2231, 3.8391, 4.5732, 5.0046]

a0, a1 = best_poly(x, y, 1)

print(f'{a0 = } e {a1 = }')