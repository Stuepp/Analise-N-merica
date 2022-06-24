import math

def richardson(col_1):
    n = len(col_1) - 1
    for i in range(n):
        for j in range(n - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]

if __name__ == '__main__':

    def func(x):
       return math.sin(x)**4 - 4*math.sin(x)**2+math.cos(x**2)+math.e**(-x**2)
    
    
    
    x0 = 0.62403
    approximations = [-3.960236265597324, -4.252453726759498, -4.368395314808069, -4.41913036258137, -4.442748148630415, -4.454128104782512]


   #  err_order = 3
    def F1(h):
        return (func(x0 + h) - func(x0)) / h

    # for o in orders:
    #    col_F1 = [F1(h/2**i) for i in range(o)]
    #    aprox = richardson(col_F1)
    #    print(f'{aprox = }')
    # col_F1 = [F1(h/2**i) for i in range(o)]
    aprox = richardson(approximations)
    print(f'{aprox = }')
       
