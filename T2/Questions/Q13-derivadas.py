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
       return x**(x**-x)


    h = 0.36246
    x0 = 1.11441
    orders = [4, 5, 6, 7, 8]

   #  err_order = 3

    #orders = [4, 5, 6, 7, 8]

    def F1(h):
        return (func(x0 + h) - func(x0)) / h

    for o in orders:
       col_F1 = [F1(h/2**i) for i in range(o)]
       aprox = richardson(col_F1)
       print(f'{aprox = }')
