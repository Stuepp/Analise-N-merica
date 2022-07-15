import numpy as np
import math

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0
    for i in range(1, n):
        sum_fx += f(a + i * h)
    return (f(a) + 2 * sum_fx + f(b)) * h / 2

def coeff_a(f, n: int, num_intervals=256):
    """
    Retorna uma aproximação
    da integral de (1/pi) * f(x)*cos(n*x)
    no intervalo -pi a pi
    """
    def func(x):
        return f(x) * np.cos(n * x)

    return trapz(func, -np.pi, np.pi, num_intervals) / np.pi

def coeff_b(f, n: int, num_intervals=256):
    """
    Retorna uma aproximação
    da integral de (1/pi) * f(x)*sin(n*x)
    no intervalo -pi a pi
    """
    def func(x):
        return f(x) * np.sin(n * x)

    return trapz(func, -np.pi, np.pi, num_intervals) / np.pi

def fourier(c, a, b):
    def func(x):
        soma = c
        for n, coeffs in enumerate(zip(a, b), 1):
            ai, bi = coeffs
            soma += (ai * np.cos(n * x) + bi * np.sin(n * x))
        return soma
    return func    

if __name__ == '__main__':

    def f(x): return 2 * math.sin(x) + math.cos(-x**2)

    num_intervals = 256
    num_coeffs = 6 # numero de termos na serie == 2 * num_coeffs + 1
    intervalo = [-1.126, 2.349]

    c = trapz(f, intervalo[0], intervalo[1], num_intervals) / (2 * intervalo[1])
    a = [coeff_a(f, ni, num_intervals) for ni in range(1, num_coeffs)]
    b = [coeff_b(f, ni, num_intervals) for ni in range(1, num_coeffs)]

    serie = fourier(c, a, b)

    # apenas para visualização
    """
    import matplotlib.pyplot as plt

    t = np.linspace(-np.pi, np.pi, 200)
    ft = [f(ti) for ti in t]

    st = [serie(ti) for ti in t]

    plt.plot(t, ft)
    plt.plot(t, st)

    plt.savefig('fourier.png')
    """