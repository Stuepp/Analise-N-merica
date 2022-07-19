import numpy as np

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = h * m2
        x0 += h
        vals.append([x0, y0])
    return vals

if __name__ == '__main__':
    def f(x, y):
        return (y + x) / 3
    
    x0, y0 = 0.633, 2.244
    h = 0.125
    n = 10
    r1 = euler(f, x0, y0, h, n)
    #print(r1)
    x1, y1 = zip(*r1)
    print(y1)

    #r2 = euler_mid(f, x0, y0, h, n)
    #x2, y2 = zip(*r2)

    def y(x):
        return (1 - x) + x + 2

    #plot 
    """
    import matplotlib.pyplot as plt

    t = np.linspace(x0, x0 + n * h, 200)
    yt = [y(ti) for ti in t]

    plt.plot(t, yt, color='blue')
    plt.scatter(x1, y1, color='orange')
    plt.scatter(x2, y2, color='magenta')

    plt.savefig('euler.png')
    """