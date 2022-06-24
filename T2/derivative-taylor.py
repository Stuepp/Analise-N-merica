
def diff1_a(f, x0, h):
    """
    Usada para aproximar a primeira
    derivada de f no ponto x0
    """
    return (f(x0 + h) - f(x0)) / h

def diff1_b(f, x0, h):
    """
    Usada para aproximar a primeira
    derivada de f no ponto x0
    """
    return (f(x0) - f(x0 - h)) / h

def diff1_c(f, x0, h):
    """
    Usada para aproximar a primeira
    derivada de f no ponto x0
    """
    return (f(x0 + h) - f(x0 - h)) / 2*h

if __name__ == '__main__':
    def f(x):
        return x**x

    x0 = 2
    hs = [10 ** (-i) for i in range(1, 10)]

    print(hs)

    for h in hs:
        print(f'diff_a(f, {x0}, {h}) = {diff1_a(f,x0, h)}')