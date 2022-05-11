import numpy as np

def best_poly(x: list[float], y: list[float], grau: int=1) -> list[float]:
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp

def modelo(x):
    a, b = -0.5, 0.5
    erro = a + (b - a) * np.random.random()
    return 2 + 2.34 * x -1.86 * x ** 2 + erro

if __name__ == '__main__':
    # x = [-2,-1,0,1,3]
    # y = [2,0,1,2,1.5]
    x = np.linspace(-3, 3, 50)
    y = [modelo(xi) for xi in x]
    grau = 2

    coefs = best_poly(x, y, grau)
    p = build_func(coefs)

    print(f'{coefs = }')

    # para vizualização
    import matplotlib.pyplot as plt

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)

    plt.savefig('best_poly.png')