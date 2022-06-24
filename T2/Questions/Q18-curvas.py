import numpy as np

#BEST_POLY

#FUNC EQUIVALENTE
# sqrt( y ) = 1/b + a/b * 1/sqrt( x )

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
    a, b = -10, 10
    erro = a + (b - a) * np.random.random()
    return 2 + 2.34 * x - 1.86 * x ** 2 - 3.21 * x ** 3 + erro


if __name__ == '__main__':
    

    
    x = [0.8501, 1.3141, 2.8246, 3.0401, 4.0302, 4.7464, 5.9947, 6.1414, 7.4909, 8.0066, 8.5805, 9.9043]
    y = [13.4736, 9.4308, 5.2463, 4.9076, 4.0658, 3.6452, 3.0707, 2.9984, 2.6489, 2.5143, 2.4454, 2.1742]
    values = [2.57, 7.2064, 8.0878]


    y_ = np.sqrt(y)
    
    x_ = 1/np.sqrt(x)

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    b = 1/a0
    a = a1 * b

    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {(a0 + a1 * 1/np.sqrt(values[xi]))**2}')
