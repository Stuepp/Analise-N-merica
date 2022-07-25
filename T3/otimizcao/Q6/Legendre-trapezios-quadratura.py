import math
import numpy as np

# add a, b, funcs, func, values = x1,x2,x3

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2
    
def P(n, x): 
    if(n == 0):
        return 1 # P0 = 1
    elif(n == 1):
        return x # P1 = x
    else:
        return (((2 * n)-1)*x * P(n-1, x)-(n-1)*P(n-2, x))/float(n)

def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck * funcao(xk)

    return soma


def change(f, a, b):
    def g(u):
        return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

    return g


if __name__ == '__main__':
 
    pontos_n10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
    pesos_n10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
    n10 = zip(pontos_n10, pesos_n10)
    
    values = [-0.928, -0.027, 0.627] #x1, x2, x3
    a = -1
    b = 1
    n = 256
    grau_legendre = 8
    #funcao
    def f(x):
        return  x * math.sin(-6 * x**2)
    
    coeffs = []
    
    for i in range(grau_legendre):
        numer = trapz(lambda x: f(x) * P(i, x), a, b, n)
        denom = trapz(lambda x: P(i, x) * P(i, x), a, b, n)
        coeffs.append(numer/denom)
    
    # imprime os coeficientes:
    for i in range(len(coeffs)):
        print(f"c{i+1}: {coeffs[i]}")    

    def g(x):
        soma = 0    
        for i in range(grau_legendre):
            mult = coeffs[i] * P(i, x)
            soma += mult
        return soma

    for x in values:
        print(f'g({x}) = {g(x)}')

    # quadratura gaussina
    exact_for_degree_less_than = 20

    def func_erro(x):
        return (f(x) - g(x))**2 #função erro

    def quadratura_zip(func_erro, pontos_e_pesos):
        soma = 0
        for x_k, c_k in pontos_e_pesos:
            soma += c_k * func_erro(x_k)
        return soma
    
    def change_zip(func_erro, a, b, u):
        return func_erro((b+a)/2 + (b-a)*u/2) * (b-a)/2
    
    def g_erro(u):
        return change_zip(func_erro, a, b, u)
    
    erro = quadratura_zip(g_erro, n10)

    #imprimindo o erro:
    print("-------------------\n")
    print("Erro: ", erro)
