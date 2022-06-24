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
       return math.cos(x)**3 + 2*math.cos(x)**2 + 1
    
    
    h = 0.43877
    x0 = -1.25167
    approximations = [0.9969253784004222, 1.2336658354901235, 1.3530323367071695]
    orders = [3]


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
       
