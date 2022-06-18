import numpy as np

def best_line(x, y):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return (b * x**2)/(a + x**2)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


c = [1.7042, 2.4044, 3.3636, 3.8399, 4.9155, 6.4006, 7.3496, 8.311, 8.4448, 9.3029, 10.9901, 11.8525]
k = [1.442, 1.9451, 2.9874, 3.171, 3.5048, 3.8089, 3.8547, 3.9345, 3.9907, 3.997, 4.1929, 4.2133]
values = [3.2505, 5.4051, 11.2368]

x = c
y = k

x_ = np.divide(1, np.power(x,2))
y_ = np.divide(1, y)

a0, a1 = best_line(x_, y_)

# kmax = b e cs = a
b = 1/a0
a = a1*b


p = build_func(a, b)

print(f'{a0 = } e {a1 = }')
print(f'{a = } e {b = }') # responder invertido

qvalues = [p(vi) for vi in values]
print(f'{qvalues = }')

#para visualização

#import matplotlib.pyplot as plt

#plt.scatter(x,y)

#t = np.linspace(min(x), max(x), 200)
#pt = [p(ti) for ti in t]

#plt.plot(t, pt, color = 'r')
#plt.savefig('best_line.png')