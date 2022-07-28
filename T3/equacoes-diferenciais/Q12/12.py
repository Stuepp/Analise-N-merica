import math # Em um circuito com tensão aplicada..

def ralston(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + 0.75 * h, y0 + 0.75 * h * m1)
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield[x0, y0]
        
def f(t, i):
    C = 0.354
    R = 1.0484
    L = 1.925
    
    return C * segunda_derivada_tensao(t) + (1/R) * derivada_tensao(t) + (1/L) * tensao(t)
    
    
def tensao(t):
    return math.exp(-0.069 * math.pi * t) * math.sin(2 * t - math.pi)
    
def derivada_tensao(t): # usar https://www.wolframalpha.com/ - exemplo de input derivative of e^(-0.059*pi*t) * sin(2 * t - pi)
    return -2*math.exp(-0.21677*t) * (math.cos(2*t) * -0.108385*math.sin(2*t))
    #return -2 * math.exp(-0.187553*t) * (math.cos(2 * t) - 0.0937765 * math.sin(2 * t))
    
def segunda_derivada_tensao(t):
    return math.exp(-0.21677*t) * (3.95301 * math.sin(2 * t) + 0.86708 * math.cos(2 * t))
    #return math.exp(-0.187553*t) * (0.750212 * math.cos(2 * t) + 3.96482 * math.sin(2 * t))

t0 = 0
i0 = 0
h = 0.0983
n = 150

r = ralston(f, t0, i0, h, n)

yt = []
for yi in r:
    yt.append(yi[1])
    
print(yt)