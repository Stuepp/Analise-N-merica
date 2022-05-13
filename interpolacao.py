import numpy as np
import math

def poly(x, y):
    n = len(x) - 1
    A = []
    B = y
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A,y)

def func_poly(x,coeffs):
    first = coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:])], 1)

def f1(x):
    return np.cos(pow(np.e,-x**2)) + np.sin(x**2/2)

def f(x):
    return pow(np.e,np.cos(x)**2) + pow(np.e,-x**2) + np.log(x)

if __name__ == '__main__':
    # exemplos
    x = [1.7,2.762,3.195,4.551,4.811]
    y = [1.121,4.694,4.28,1.765,1.615]

    # exempl 2
    #x = [0, np.pi / 2, np.pi]
    #y = [0,1,0]
    #x = [0.77,2.205,3.275]
    #y = []
    #for i in x:
    #    y.append(f1(i))
    
    coeffs = poly(x,y)
    print(coeffs)
    #print([ai + j*0 for j, ai in enumerate (coeffs[0:], 0)])
    def p(x):
        return func_poly(x, coeffs)
    #valores de x
    print(p(2.164))
    print(p(3.265))
    print(p(4.574))

    #visualização
    # import matplotlib.pylab as plt
    
    # plt.scatter(x,y)

    # t = np.lenspace(min(x), 200)
    # pt = [p(ti) for ti in t]
    #funão seno exemplo 2
    # st = np.sin(t)

    # plt.plot(t,pt)
    # plt.plot(t,st)

    # plt.savefig(inter.png)