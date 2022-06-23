import math

def quadratura(f, x: list, c: list): return sum([ci * f(xi) for ci, xi in zip(c, x)])

def change(f, a, b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g

if __name__ == '__main__':
    x = (
        -0.39,
        0.33,
        -0.86,
        0.86
    )
    c = (
        0.65,
        0.65,
        0.34,
        0.34
    )
    nos = {
        2: (-0.5773502691896257, 0.5773502691896257),
        3: (0, -0.7745966692414834, 0.7745966692414834),
        4: (-0.33998104358485626, 0.33998104358485626, -0.8611363115940526, 0.8611363115940526),
        5: (0, -0.5384693101056831, 0.5384693101056831, -0.906179845938664, 0.906179845938664),
        6: (0.6612093864662645, -0.6612093864662645, -0.2386191860831969, 0.2386191860831969, -0.932469514203152, 0.932469514203152),
        7: (0, 0.4058451513773972, -0.4058451513773972, -0.7415311855993945, 0.7415311855993945, -0.9491079123427585, 0.9491079123427585),
        8: (-0.1834346424956498, 0.1834346424956498, -0.525532409916329, 0.525532409916329, -0.7966664774136267, 0.7966664774136267, -0.9602898564975363, 0.9602898564975363),
        9: (0, -0.8360311073266358, 0.8360311073266358, -0.9681602395076261, 0.9681602395076261, -0.3242534234038089, 0.3242534234038089, -0.6133714327005904, 0.6133714327005904),
        10: (-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717)
    }
    pesos = {
        2: (1.0, 1.0),
        3: (0.8888888888888888, 0.5555555555555556, 0.5555555555555556),
        4: (0.6521451548625461, 0.6521451548625461, 0.34785484513745385, 0.34785484513745385),
        5: (0.5688888888888889, 0.47862867049936647, 0.47862867049936647, 0.23692688505618908, 0.23692688505618908),
        6: (0.3607615730481386, 0.3607615730481386, 0.46791393457269104, 0.46791393457269104, 0.17132449237917036, 0.17132449237917036),
        7: (0.4179591836734694, 0.3818300505051189, 0.3818300505051189, 0.27970539148927664, 0.27970539148927664, 0.1294849661688697, 0.1294849661688697),
        8: (0.362683783378362, 0.362683783378362, 0.31370664587788727, 0.31370664587788727, 0.22238103445337448, 0.22238103445337448, 0.10122853629037626, 0.10122853629037626),
        9: (0.3302393550012598, 0.1806481606948574, 0.1806481606948574, 0.08127438836157441, 0.08127438836157441, 0.31234707704000286, 0.31234707704000286, 0.26061069640293544, 0.26061069640293544),
        10: (0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814)
    }

    def f_1(x): return math.exp(-x**2)
    def f_2(x): return math.log(math.sqrt(1+x**2))
    def f_3(x): return math.exp(x)*math.sin(x)/(1+x**2)
    def f_4(x): return math.cos(-x**2/3)
    def f_5(x): return (x+1/x)**2

    #aprox = quadratura(f_1, x, c)

    #print(f'{aprox_1 = }')

    #for i in  range(2, 6):
    #    aprox_2 = quadratura(f_1, x=nos[i], c=pesos[i])

    a = (-0.631, 1.96, 0.163, -1.017, 0.894)
    b = (0.908, 3.034, 2.413, 1.43, 2.066)
    #g = {change(f_1, a[i], b[i]), change(f_2, a[i], b[i]), change(f_3, a[i], b[i]), change(f_4, a[i], b[i]), change(f_5, a[i], b[i]), }
    k = (4, 8, 12, 6, 10)

    for i in range(2, 10):
        g = change(f_5, a[4], b[4])
        aprox = quadratura(g, x=nos[i], c=pesos[i])
        print(f'{aprox = } exata em poly de grau menor que {2*i} i = {i}')