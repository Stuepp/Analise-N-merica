import math
import numpy as np

def romberg(array):
    # i = 0  está calculando a coluna F2
    error_order = 8
    numCols = error_order / 2.0 - 1
    for i in range(int(numCols)):
        for j in range(int(numCols)):
            numer = (2  ** ((i + 1) * 2)) * array[j + 1] - array[j]
            denom = (2 ** ((i + 1) * 2)) - 1
            array[j] = numer / denom
    print(f'Aprox O(h^{error_order}) = {array[0]}')

def trapz(f, a, b, n):
    # Regra dos Trapézios para aproximar integrais
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma

def best_func(f, funcs, a, b, n):
    k = len(funcs)
    # constroí uma matriz k x k cheia de zeros
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []
    for i in range(0, k):
        for j in range(0, k):
            # preenche a matriz A
            if j >= i:
                def f_ij(x):
                    return funcs[j](x) * funcs[i](x)
                hs = [h / 2 ** i for i in range(ki)]
                col1 = [trapz(f_ij, a, b, hi) for hi in hs]
                integral_ij = romberg(col1)
                A[i][j] = integral_ij
            else:
                A[i][j] = A[j][i]
        # preencher a matriz B
        def ffi(x):
            return f(x) * funcs[i](x)
        hs = [h / 2 ** i for i in range(ki)]
        col1 = [trapz(ffi, a, b, hi) for hi in hs]
        B.append(romberg(col1))
    return np.linalg.solve(A, B)

# exemplo
a = -2.113
b = 2.112
n = 10

def f(x): return x**2 * math.cos(x * math.sin(math.log(1 + x**2)))
def f1(x): return 2
def f2(x): return x - 1
def f3(x): return x**2 + 1
def f4(x): return x**3 + x - 3
def f5(x): return 0.5 * x**4 - 3 * x**2 + 1
def f6(x): return x**5 - 4 * x + 2
def f7(x): return x**7-x

funcs = [f1, f2, f3, f4, f5, f6, f7]

coefs = best_func(f, funcs, a, b, n)
print('coefs')

for i in range(len(coefs)):
    print(f'{coefs[i]}')



"""
coluna_F1= []
for i in range(8):
    coluna_F1.append(trapz(f, a, b, n))
romberg(coluna_F1)
"""

def g(x):
    soma = 0
    for k in range(len(coefs)):
        soma += coefs[k]*funcs[k](x)
    return soma

xis = [-1.045, -0.103, 1.013]

print('xis:')
print(g(xis[0]))
print(g(xis[1]))
print(g(xis[2]))