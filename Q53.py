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
    x = [-0.652, -0.111, 0.506]
    #x = [1.187, 3.697, 5.043, 7.107, 8.577]
    y = []
    def f(x):
        # função f(x) aqui
        return 1 / (1 + 25*x*x)
    
    def f2(x):
        return pow(np.e,np.cos(x)**2) + pow(np.e,-x**2) + np.log(x)

    for xi in x:
        y.append(f(xi))

    coeffs = poly(x,y)
    
#imprime coeffs:
    #for x in (coeffs):
        #print("%.16f" %x)

#calcula valores de x
    def p(x):
        return func_poly(x,coeffs)        

# calcula f(x) - p(x):
print(abs(f(0.53) - p(0.53)))
print(abs(f(0.945) - p(0.945)))
#print(abs(f2(3.847) - p(3.847)))
#print(abs(f2(7.288) - p(7.288)))
#print(abs(f2(7.913)- p(7.913)))    