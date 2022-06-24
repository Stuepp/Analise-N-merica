from re import A
import numpy as np

#BEST_EXP


def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x*np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':


    x = [1.5999, 1.8741, 3.0632, 3.7808, 4.0724, 5.3574, 5.6449, 6.5623, 7.186, 7.7601, 9.2132, 9.3811]
    y = [4.1834, 4.5153, 5.4472, 5.9019, 6.0419, 6.5407, 6.6713, 6.9451, 7.1671, 7.1877, 7.6817, 7.7244]
    values = [4.343, 5.5108, 7.2737]


    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    x_ = np.log(x)

    y_ = y

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = a1
    b = a0

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'y(x{xi+1}) = {a0+a1*np.log(values[xi])}')

    p = build_func(a, b)

    def q(x):
        return p(x) - k
