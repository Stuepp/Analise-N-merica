def dif_div(x: list[float], y: list[float]) -> list[float]:
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num-1):
        for i in range(num -1 - j):
            numer = Y[i+1] - Y[i]
            denom = x[i + 1 + j] - x[i]
            div = numer / denom
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t,x,coefs)
    return temp

if __name__ == '__main__':
    # exemplo
    # (1,0),(2,1),(3,5),(4,1)
    x = [1,2,3,4]
    y = [0,1,5,1]

    coefs = dif_div(x,y)
    # o polinômio interpolador da lista de pontos
    p = build_func(x, coefs)

    print(coefs)
    print(p(1), p(2), p(3), p(4))

    # vizualização
    import matplotlib.pyplot as plt
    import numpy as np

    t = np.linspace(min(x), max(x), 100)
    pt = [p(ti) for ti in t]

    plt.scater(x,y) # pontos
    plt.plot(t,pt) # gráfico de p

    plt.savefig('dif_div.png')