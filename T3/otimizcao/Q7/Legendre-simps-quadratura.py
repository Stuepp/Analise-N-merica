import math
import numpy as np

def simps(f, a, b, n):
    if(n % 2 != 0):
        print('O número de subintervalos deve ser par')
        return
    int(numParabolas) = n / 2
    soma = 0
    h = (b - a) / n
    for k in range(numParabolas):
        x0 = a + (2 * k) * h
        x1 = a + (2 * k + 1) * h
        x2 = a + (2 * k + 2) * h
        soma += (f(x0) + 4*f(x1) + f(x2))
    soma *= h/3
    print(f'Area aprox: {soma}')
    
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
    
    values = [-0.559, -0.18, 0.637] #x1, x2, x3
    a = -1
    b = 1
    n = 128
    grau_legendre = 12
    #funcao
    def f(x):
        return x * math.cos(10 * x**2 * math.exp(-x**2))
    
    coeffs = []
    coeffs = simps(f, a, b, n)
    
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
    
    #imprimindo o erro:
    print("-------------------\n")
    print("Erro: ", erro)
