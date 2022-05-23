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
    return a * x ** b

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp

def modelo(x):
    a, b = 1, 20
    erro = a + (b - a) * np.random.random()
    return 2.3 *x ** 3.89 + erro

if __name__ == '__main__':

    x = np.linspace(1, 3, 20)
    print(f'{x = }')
    y = [modelo(xi) for xi in x]

    x_ = np.log(x)
    y_ = np.log(yt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    # para visualização
    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [q(ti) for ti in t]

    plt.plot(t, pt, color='r')

    plt.savefig('best_exp.png')