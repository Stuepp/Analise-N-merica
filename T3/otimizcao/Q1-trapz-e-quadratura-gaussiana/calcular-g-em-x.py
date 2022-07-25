import math
import numpy as np

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
                integral_ij = trapz(f_ij, a, b, n)
                A[i][j] = integral_ij
            else:
                A[i][j] = A[j][i]
        # preencher a matriz B
        def ffi(x):
            return f(x) * funcs[i](x)
        B.append(trapz(ffi, a, b, n))
    return np.linalg.solve(A, B)

# exemplo
a = -1.126
b = 2.349
n = 256

def f(x): return 2 * math.sin(x) + math.cos(-x**2)
def f1(x): return 1
def f2(x): return x
def f3(x): return x**2
def f4(x): return x**3
def f5(x): return x**4
def f6(x): return x**5

funcs = [f1, f2, f3, f4, f5, f6]

coefs = best_func(f, funcs, a, b, n)
for i in range(len(coefs)):
    print(f'coefs: {coefs[i]}')

def g(x):
    soma = 0
    for k in range(len(coefs)):
        soma += coefs[k]*funcs[k](x)
    return soma

xis = [-0.493, 0.664, 1.981]

print(g(xis[0]))
print(g(xis[1]))
print(g(xis[2]))