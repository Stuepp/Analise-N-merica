import numpy as np

def true_euler(f, x0, y0, h, n):#euler normal mas funcionando
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h        
        print(f'x_{k + 1}={x0} e y_{k+1}={y0}')

def euler_mid(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

def heun(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1 + m2) / 2
        x0 += h
        yield [x0, y0]

def ralston(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + 0.75*h, y0 + 0.75*h * m1)
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield [x0, y0]


if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1
    
    x0, y0 = 0.483, 1.299
    h = 0.15
    n = 10
    """
    r1 = true_euler(f, x0, y0, h, n)
    print(r1)
    x1, y1 = zip(*r1)
    print(y1)
    """
    """
    r2 = euler_mid(f, x0, y0, h, n)
    x2, y2 = zip(*r2)
    print(y2)
    """
    """
    r3 =  heun(f, x0, y0, h, n)
    #print(list(r3))
    #print(next(r3))
    x3, y3 = zip(*r3)
    print(y3)
    """
    r4 =  ralston(f, x0, y0, h, n)
    x4, y4 = zip(*r4)
    print(y4)

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