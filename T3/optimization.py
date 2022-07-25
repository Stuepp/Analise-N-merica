import numpy as np
import math

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0
    for i in range(1, n):
        sum_fx += f(a + i * h)
    return (f(a) + 2 * sum_fx + f(b)) * h / 2

def coeffs(func, funcs):
    n = len(funcs)
    A = np.zeros((n, n), dtype=float)
    B = np.zeros(n, dtype=float)
    for i in range(n):
        for j in range(i, n):
            def f_ji(x):
                return funcs[j](x) * funcs[i](x)
            """
            Produto de f_j e f_i cuja integral
            vive na posição i, j
            """
            # Resolver as integrais, adaptável
            A[i][j] = trapz(f_ji, a=1, b=2, n=256)
            if i != j:
                A[j][i] = A[i][j]
        ffi = lambda x: func(x) * funcs[i](x)
        # Resolver as integrais, adaptável
        B[i] = trapz(ffi, a=1, b=2, n=256)
    return np.linalg.solve(A, B)
    
    def build_func(s, var: str='x'):
        scope = {}
        scope['math'] = math
        func = f'def f({var}): return {s}'
        exec(func, scope)
        return scope['f']
    
    if __name__ == '__main__':
        def func(x):
            return np.exp(-x**2) * np.cos(np.sqrt(x))

        funcs_str = ['x+1','math.cos(x)','math.exp(x)','math.lof(x)']
        funcs[]
        for func_str in funcs_str:
            f = build_func(func_str)
            funcs.append(f)
        
        c = coeffs(func, funcs)
        print(c)
        
# ALGO FOI COPIADO ERRADO!!!
# https://www.youtube.com/watch?v=mVsLAp3bxMg
