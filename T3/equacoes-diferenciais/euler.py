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

def ralston_pontos_especificios(f, x0, y0, hs, n):
    for i in range(n):
        h = hs[i]
        m1 = f(x0, y0)
        m2 = f(x0 + 0.75*h, y0 + 0.75*h * m1)
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield [x0, y0]

def RK2(f, x0, y0, h, n, b: int=1):
    """
    Método de Runge-Kutta geral de ordem 2
    Por padrão usa o Método do Ponto Médio de Euler
    que corresponde a b = 1
    b = 1/2 corresponde ao Método de Heun
    b = 1/3 corresponde ao Método de Ralston
    """
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p * h, y0 + q * h * m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h 
        yield[x0, y0]

def RK4(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        #yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6 # 
        # atualizar x0 e  y0
        x0 += h
        #y0 = yk
        y0 += h * (m1 + 2 * m2 + 2 * m3 + m4) / 6
        yield[x0, y0]

if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1
    
    x0, y0 = 0.284, 2.092
    b = 0.913
    h = 0.189
    n = 10
    xs = [x0, 0.51, 0.874, 1.048, 1.259, 1.683, 1.858, 2.031, 2.404, 2.697, 2.823]
    hs = []
    for i in range(len(xs)-1):
        hs.append(xs[i+1]-xs[i])
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
    """
    r4 =  ralston(f, x0, y0, h, n)
    x4, y4 = zip(*r4)
    print(y4)
    """
    """
    r5 = RK2(f,x0, y0, h, n, b)
    x5, y5 = zip(*r5)
    print(y5)
    """
    """
    r6 = RK4(f,x0, y0, h, n)
    x6, y6 = zip(*r6)
    print(y6)
    """
    # pontos exatos
    r7 = ralston_pontos_especificios(f,x0,y0, hs, n)
    x7,y7 = zip(*r7)
    print(y7)

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