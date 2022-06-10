import math

def p(x):
    return 1 - 3 * x + 4 * x**2 - 2 * x**3

r = math.sqrt(3) / 3

aprox = p(-r) + p(r)

print(f'{aprox = }')

def f(x):
    return math.exp(-x**2)

aprox = f(-r) + f(r)

print(f'{aprox = }')