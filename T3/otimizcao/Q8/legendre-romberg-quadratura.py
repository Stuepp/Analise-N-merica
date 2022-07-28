import math
import numpy as np

def legendre(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre(x, n - 1) - (n - 1) * legendre(x, n - 2)) / n

def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck * funcao(xk)

    return soma

def change(f, a, b):
    def g(u):
        return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

    return g

def build_legendre_polynomial(n):
    def temp(t):
        return legendre(t, n)
    return temp

def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * coluna_f1[i + 1] - coluna_f1[i]) / (4 ** power - 1)
        coluna_f1[:n - 1 - j] = temp_col
        # print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]

def trapz_romberg(f, a, b, h):
    n = int((b - a) / h)
    soma = 0

    for k in range(1, n):
        soma += f(a + k * h)

    return (h / 2) * (f(a) + 2 * soma + f(b))

def best_func(f, funcs, a, b, order, h):
    k = len(funcs)

    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []

    for i in range(k):
        for j in range(k):
            if i == j:
                if j >= i:
                    def f_ij(x):
                        return funcs[j](x) * funcs[i](x)
                    tam = int(order / 2)
                    hs = [h / 2 ** ki for ki in range(tam)]
                    coluna_f1 = [trapz_romberg(f_ij, a, b, hi) for hi in hs]
                    A[i][j] = romberg(coluna_f1)

                else:
                    A[i][j] = A[j][i]

        def ffi(x):
            return f(x) * funcs[i](x)

        tam = int(order / 2)
        hs = [h / 2 ** ki for ki in range(tam)]
        coluna_f1 = [trapz_romberg(ffi, a, b, hi) for hi in hs]
        B.append(romberg(coluna_f1))
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    return np.linalg.solve(A, B)

if __name__ == '__main__':
 
    raiz10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
    peso10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
    n10 = zip(raiz10, peso10)
    
    values = [-0.826, 0.073, 0.732] #x1, x2, x3
    a = -1
    b = 1
    n = 128
    order = 8
    h = 2/16
    grau_legendre = 16
    #method = ['simps', 128]
    funcs = [build_legendre_polynomial(i) for i in range(grau_legendre)]
    #funcao
    def f(x):
        return math.tanh(3 * x) * math.cos(3 * x)
    
    coefs = best_func(f, funcs, a, b, order, h)

    coefs = [ci for ci in coefs]

    print(f'Coeficientes: {coefs}')  

    def g(x):
        return sum(ci * fi(x) for ci, fi in zip(coefs, funcs))

    for x in values:
        print(f'g({x}) = {g(x)}')

    # quadratura gaussina
    exact_for_degree_less_than = 20

    def func_erro(x):
        return (f(x) - g(x))**2 #função erro
    
    order = str(int(exact_for_degree_less_than / 2))
    txt_order = ['raiz' + order, 'peso' + order]

    erro = quadratura(change(func_erro, a, b), locals()[txt_order[0]], locals()[txt_order[1]])

    print(f'{erro = }')
