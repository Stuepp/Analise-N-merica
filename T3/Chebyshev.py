import numpy as np

def coeffs(x, y):
    n = len(x)
    A = np.zeros((n,n), dtype=float)
    for i in range(n):
        xi = x[i]
        for j in range(n):
            if j == 0:
                A[i][j] = 1.0
            else:
                A[i][j] = xi ** j
    y = np.array(y, dtype=float)
    return np.linalg.solve(A, y)

def poly(c):
    def temp(x):
        return sum(ci * x ** i for i, ci in enumerate(c))
    return temp

def f(x):
    return 1 /(1 + pow(x, 2))

n = 3 # número de pontos para a interpolação
xp = [np.cos((2 * k + 1) * np.pi / (2 * n)) for k in range(n)]
fp = [f(xi) for xi in xp]

# plotar o gráfico do polinômio interpolador nessa lista de pontos
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 256)
c = coeffs(xp, fp)
interp = poly(c)
pt = [interp(ti) for ti in t] # gráfico do polinômio interpolador

ft = [f(ti) for ti in t]

plt.plot(t, ft, color='blue')
plt.plot(t, pt, color='orange')

plt.savefig('chebyshev.png')