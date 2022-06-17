import numpy as np

def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first=coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
    #valores das listas
    x=[1.95, 2.815, 3.308, 4.345, 4.784]
    y=[1.526, 4.529, 4.838, 3.274, 1.385]

    coeffs = poly(x,y)
    #print(coeffs)

#imprime coeffs:
    #for x in (coeffs):
        #print("%.16f" %x)
    
    #calcula valores de x
    def p(x):
        return func_poly(x,coeffs)
    # valores dos x:
    print(p(1.529))
    print(p(1.874))
    print(p(2.726))
        
    