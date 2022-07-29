import math

"""
 Em um circuito com tensão aplicada E e com resistência R, indutância L e capacitância
 C em paralelo, a corrente i satisfaz a equação diferencial
 ....
 use o método de Heun para encontrar estimativas para a corrente i nos pontos
 .....
"""

def heun(f, x0, y0, h_values, n):
    for k in range(n):
        h = h_values[k]
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1 + m2) / 2
        x0 += h
        yield[x0, y0]
        
def f(t, i):
    C = 0.3115
    R = 1.2392
    L = 1.8724
    
    return C * segunda_derivada_tensao(t) + (1/R) * derivada_tensao(t) + (1/L) * tensao(t)
    
    
def tensao(t):
    expoente = -0.0708
    # calcular 1 e 2 derivada no wolfram
    # e^(expoente*pi*t) * sin(2 * t - pi) 
    return math.exp(expoente * math.pi * t) * math.sin(2 * t - math.pi)
    
def derivada_tensao(t):
    expo1 = -0.222425
    coef = -0.111212
    return -2 * math.exp(expo1*t) * (math.cos(2 * t) + coef * math.sin(2 * t))
    
def segunda_derivada_tensao(t):
    expoe = -0.222425
    coefcos = 0.889698
    coefsin = 3.95053
    
    return math.exp(expoe*t) * (coefcos * math.cos(2 * t) + coefsin * math.sin(2 * t))

t0 = 0
i0 = 0
t_values = [0.0801, 0.1545, 0.2856, 0.3162, 0.434, 0.5698, 0.6385, 0.7657, 0.8781, 0.9526, 1.0555, 1.1435, 1.2256, 1.318, 1.4363, 1.5405, 1.6763, 1.7139, 1.8404, 1.9588, 2.0404, 2.1231, 2.2442, 2.3884, 2.4508, 2.5806, 2.6378, 2.7456, 2.8597, 2.9442, 3.0369, 3.1385, 3.2269, 3.3707, 3.432, 3.5524, 3.661, 3.7265, 3.8667, 3.94, 4.0704, 4.1822, 4.2517, 4.3355, 4.4469, 4.5219, 4.6789, 4.7626, 4.811, 4.9669, 5.0776, 5.181, 5.2603, 5.3175, 5.4586, 5.5251, 5.6544, 5.7598, 5.8141, 5.9262, 6.044, 6.1555, 6.25, 6.3208, 6.4388, 6.5495, 6.6429, 6.7409, 6.8107, 6.9365, 7.0228, 7.1663, 7.2192, 7.3172, 7.4795, 7.5414, 7.6485, 7.7361, 7.8252, 7.933, 8.0381, 8.1324, 8.241, 8.3568, 8.4473, 8.5308, 8.6809, 8.7624, 8.8242, 8.9223, 9.06, 9.1689, 9.2608, 9.3662, 9.4126, 9.5377, 9.6142, 9.7493, 9.8647, 9.9791, 10.0309, 10.1846, 10.2553, 10.3294, 10.454, 10.5269, 10.6567, 10.7452, 10.8716, 10.9576, 11.0848, 11.1763, 11.254, 11.3111, 11.4629, 11.5792, 11.6107, 11.7615, 11.8569, 11.9425, 12.0514, 12.1688, 12.2513, 12.3753, 12.4602, 12.5178, 12.6226, 12.7849, 12.8811, 12.9738, 13.0468, 13.1757, 13.231, 13.3271, 13.4845, 13.5597, 13.6157, 13.7809, 13.8365, 13.9475, 14.0224, 14.1806, 14.2159, 14.3713, 14.4589, 14.564, 14.6285, 14.7349, 14.8547, 14.9719]
n = 150

t_values.insert(0, t0)
h_values = []
for i in range(len(t_values)-1):
    h_values.append(t_values[i+1] - t_values[i])

r = heun(f, t0, i0, h_values, n)

yt = []
for yi in r:
    yt.append(yi[1])
    
print(yt)