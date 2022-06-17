def langrange(x,y):
    # retorna yi dividido pelo denominador do polinômio Li
    num = len(x)
    coefs = []
    for i in range(num):
        prod = 1
        for j in range(num):
            if i != j:
                prod *= (x[i] - x[j])
        ci = y[i] / prod
        coefs.append(ci)
    return coefs

def pl(t: float, x: list[float], coefs: list[float]) -> float:
        soma = 0
        num = len(coefs)
        for i in range(num):
            prod = 1
            for j in range(num):
                if(i != j):
                    prod *= (t-x[j])
            prod *= coefs[i]
            soma += prod
        return soma

def poly(x, coefs):
    def f(t):
        return pl(t,x,coefs)
    return f

if __name__ == '__main__':
    # exemplo
    x = [1, 2, 4]
    y = [0, 3, -1]
    c = langrange(x,y) # c coeficientes

    lagr = poly(x,c)

    print(langrange(x,y))
    print(lagr(1), lagr(2), lagr(4))

    # visualização
    import matplotlib.pyplot as plt
    import numpy as np

    plt .scatter(x,y)

    t = np.linspace(min(x), max(x), 100)
    lt = [lagr(ti) for ti in t]

    plt.plot(t, lt)

    plt.savefig('lagrange.png')